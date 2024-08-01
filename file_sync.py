import filecmp
import os
import shutil


def compare_and_copy(source_dir, target_dir, exclude_files=None, exclude_paths=None):
    if exclude_files is None:
        exclude_files = []
    if exclude_paths is None:
        exclude_paths = []

    # 遍历源目录和目标目录
    for root, dirs, files in os.walk(source_dir):
        # 计算相对路径
        relative_path = os.path.relpath(root, source_dir)

        # 跳过排除的路径
        should_continue = False
        for exclude_path in exclude_paths:
            if exclude_path in relative_path:
                should_continue = True
        if should_continue:
            continue

        # 确定目标目录中的对应目录
        target_root = os.path.join(target_dir, relative_path)

        # 确保目标目录存在
        if not os.path.exists(target_root):
            os.makedirs(target_root)

        for file in files:
            # 跳过排除的文件
            if file in exclude_files:
                continue

            source_file_path = os.path.join(root, file)
            target_file_path = os.path.join(target_root, file)

            # 如果目标文件存在且内容不同，或者目标文件不存在，复制文件
            if os.path.exists(target_file_path):
                if not filecmp.cmp(source_file_path, target_file_path, shallow=False):
                    print(f"文件 {source_file_path} 存在但内容不同，复制到目标文件夹")
                    shutil.copy2(target_file_path, source_file_path)


# 示例使用
source_dir = './'  # 源文件夹路径
target_dir = '../faker3'  # 目标文件夹路径
exclude_files = []  # 排除的文件列表
exclude_paths = ['.git', '.idea']  # 排除的路径列表

compare_and_copy(source_dir, target_dir, exclude_files, exclude_paths)

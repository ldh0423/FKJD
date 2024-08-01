import os
import shutil
import requests
import re

# Step 1: 从网站中抓取内容
url = 'https://raw.githubusercontent.com/shufflewzc/AutoSpy/master/config/Faker.spy'  # 请替换为目标网站的URL
response = requests.get(url)
if response.status_code == 200:
    content = response.text
else:
    raise Exception(f"Failed to fetch content from {url}")

# Step 2: 在抓取的内容中使用正则表达式提取 `Script:` 后的文件名
pattern = re.compile(r'Script: \s*(\w+\.js)')
matched_files = pattern.findall(content)


# Step 3: 检查指定文件夹中是否有这些文件，并复制到目标文件夹
source_folder = '../faker3/'  # 请替换为源文件夹路径
destination_folder = './'  # 请替换为目标文件夹路径

for file_name in matched_files:
    source_file_path = os.path.join(source_folder, file_name)
    destination_file_path = os.path.join(destination_folder, file_name)

    if os.path.exists(source_file_path):
        shutil.copy(source_file_path, destination_file_path)
        print(f"文件 {file_name} 已成功复制到 {destination_folder}")
    else:
        print(f"文件 {file_name} 在 {source_folder} 中不存在")

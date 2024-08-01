import os
import shutil
import requests
import yaml

url = 'https://raw.githubusercontent.com/shufflewzc/AutoSpy/master/config/Faker.spy'  # 请替换为目标网站的URL
response = requests.get(url)
if response.status_code == 200:
    content = response.text
else:
    raise Exception(f"Failed to fetch content from {url}")

data = yaml.safe_load(content)

source_folder = '../faker3/'
destination_folder = './'

for Container in data["js_config"]:

    file_name = Container["Script"]
    source_file_path = os.path.join(source_folder, file_name)
    destination_file_path = os.path.join(destination_folder, file_name)

    if os.path.exists(source_file_path):
        shutil.copy(source_file_path, destination_file_path)
        print(f"文件 {file_name} 已成功复制到 {destination_folder}")
    else:
        print(f"文件 {file_name} 在 {source_folder} 中不存在")

    Container["Script"] = "ldh0423_FKJD/" + Container["Script"]

with open('Faker.spy', 'w', encoding='utf-8') as file:
    yaml.dump(data, file, allow_unicode=True, default_flow_style=False)

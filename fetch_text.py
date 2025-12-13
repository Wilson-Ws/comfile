import requests
import json
import os

# 读取仓库根目录中的清单文件
with open('config.json', 'r', encoding='utf-8') as f:
    config_data = json.load(f)

# 基础 URL
base_url = "https://kelee.one/Tool/Loon/Lpx"

# 自定义请求头
headers = {
    "User-Agent": "Loon/917 CFNetwork/3826.600.41 Darwin/24.6.0",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN;q=0.9,zh-Hans;q=0.8",
}

# 遍历清单中的每一项
for item in config_data:
    filename_prefix = item["filename"]
    
    # 动态生成目标 URL
    url = f"{base_url}/{filename_prefix}.lpx"

    # 发起 GET 请求
    response = requests.get(url, headers=headers)

    # 检查请求是否成功
    if response.status_code == 304:
        text_content = response.text
        
        # 动态生成保存文件的路径
        filename = f"{filename_prefix}.lpx"
        
        # 将内容保存到文件中
        with open(filename, "w", encoding="utf-8") as f:
            f.write(text_content)
        print(f"内容已成功保存到 {filename}")
    else:
        print(f"请求失败，状态码: {response.status_code}，URL: {url}")

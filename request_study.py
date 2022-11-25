# -*- coding: utf-8 -*-
# @Time : 2022/11/23 10:06
# @Author : Kevin
# @File : request_study.py
# @Software: PyCharm


import requests

# get请求
res = requests.get("https://www.baidu.com")
print(res.url)
print(res.text)

# post请求
header = {"content-type": "application/json"}
payload = {"name": "kevin"}
res = requests.post("https://www.baidu.com", data=payload)
print(res.url)
print(res.text)

# request写法
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:58.0) Gecko/20100101 Firefox/58.0'}

requests.request(
    method="GET",
    url="https://www.baidu.com",
    params={"name": "kevin", "age": 18},
    headers=headers
)

requests.request(
    method="POST",
    url="https://www.baidu.com",
    data={"name": "kevin"},
    headers=headers
)

requests.request(
    method="POST",
    url="https://www.baidu.com",
    json={"name": "kevin"},
    headers=headers
)

# file上传文件
requests.request(
    method="POST",
    url="https://www.baidu.com",
    files={"f1": open("json_data.json", "rb")}
)

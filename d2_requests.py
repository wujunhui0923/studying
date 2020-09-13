#!usr/bin/python
#-*- coding = utf-8 -*-

import requests
# 发送post请求，传递参数的方式，
# 传递参数可以通过表单形式
form_data = {"form_admin": "benzi"}
# 传递参数可以通过json格式传递
url = "https://api.github.com"
headers = {"token": "12233", "name": "zhansan"}
data = {"name": "XiaoLi", "pwd": "123456"}
json_data = {"dalao": "lisi"}
res = requests.post(url, form_data, json_data,  params=data, headers=headers)


# 获取响应文本，数据类型的格式，string格式
print(res.txt)

# 获取二进制格式的
print(res.content)

# 获取json格式,,,数据类型为字典，，，，dictionary
print(res.json())
print(type(res.json()))




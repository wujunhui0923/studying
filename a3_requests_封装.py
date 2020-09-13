#!usr/bin/python
#-*- coding = utf-8 -*-


import requests

# 访问接口
url = "http://120.78.128.25:8766/futrueloan/member/register"
headers = {"X-lemonban-Media-Type": "lemonban.V2"}
data = {"mobile_phone": "18111112222", "pwd": "12344567"}
# 一定需要添加headers关键字，不能以位置参数进行传递，因为headers放到了不定长参数里面
res = requests.post(url, json=data, headers=headers)
# content-type,不需要进行添加，json关键字参数就是表示content-type = json,
# data 关键字参数就是表单格式
#  params参数就是表示query string
#
print(res.json())


# 登录接口
# token放到请求头还是请求体中，根据后端开发人员提供的操作手册，请求头或请求体中
# cookie仅能放到请求头当中，HTTP协议规定的
url = "http://120.78.128.25:8766/futrueloan/member/login"
headers = {"X-lemonban-Media-Type": "lemonban.V2"}
data = {"mobile_phone": "18111112222", "pwd": "12344567"}

res = requests.post(url, json=data, headers=headers)
# print(res.json())

# 充值
recharge_url = "http://120.78.128.25:8766/futrueloan/member/recharge"
token = res.json()['data']['token_info']['token']
id = res.json()['data']['id']
headers ={"X-lemonban-Media-Type": "lemonban.V2", "Authorization": "Bearer {}".format(token)}

data = {
    "member_id" :"id",
    "amount" :100
}
res = requests.post(recharge_url,json=data, headers=headers)
print(res.json())

# cookie 值的用法，没有token的情况



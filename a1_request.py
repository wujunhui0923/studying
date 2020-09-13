#!usr/bin/python
#-*- coding = utf-8 -*-

"""
模块导入的时候用到的
内置模块：python 自己自带的文件
自己写的模块
别人写的模块，第三方库/模块


request  仓库，第三方库，是需要安装的
pip install requests
第三方库安装的两种方式

输入命令： pip install  库名 <在命令行中输入命令行>
在setting 中进行安装的
File---settings----project untitled----project Interpreter  ,点击加号，搜索需要安装胡
的库名，点击下方的install 按钮进行安装

"""
# 导入request
import requests
# 访问一个url接口地址，发送一个GET请求

# url = "http://api.github.com"
# res = requests.get(url)
# print(res.text)  # <Response [200]>

# 如何传递参数，修改请求头，token

headers = {"name": "张三", "token": "123"}
url = "http://api.github.com"

data = {"username": "li ming", "pwd": "111"}
# 如何传递参数，，位置参数/关键字参数  params
# 其中params 为位置参数，可以将其省略，headers为可变参数，不能省略的
# res = requests.get(url, data, headers=headers)
res = requests.get(url, params=data, headers=headers)
# get请求通过query string查询字符串的方式传递的，

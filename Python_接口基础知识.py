#!usr/bin/python
#-*- coding = utf-8 -*-

"""
 当值为False，'',[],{},0,None()
 if V:
    为False



"""


class Phone:
    def call(self):
        print("正在打电话")


class SmartPhone(Phone):

    def record(self):
        print("正在录音")

    def call(self, record=False):
        """False,'',[],0,None"""
        if record:
            self.record()
        super().call()


class Iphone(SmartPhone):

    def face_time(self):
        print("正在facetime")

    def call(self, record=False, face_time=False):
        if face_time:
             self.face_time()
        super().call()


"""
excel的操作
"""
class ExcelManual:

    def __init__(self, file):
        self.file = file

    def get_sheet(self, name):
        pass

    def read_cell(self, row, column):
        pass

    def change_cell(self, row, new_column):
        pass


"""
常见的接口类型：http,https,webservices,dubbo, 

用户代理：
user-agent
content-type   请求数据格式

请求状态码

200  请求成功  201 创建成功后返回---post
304 未改变，已缓存，从缓存中读取   重定向   <从新请求新的地址
301   永久重定向，302  临时重定向>
404 找不到资源   NOT FOUND
401  没有权限
405 请求方法不允许

二、响应头
content-type

application/json
txt/html
set-cookie

三次握手



四次挥手:


输入url的过程
a.先输入url,DNS域名解析
b.三次握手
c.前端渲染
d.显示在前端页面







"""



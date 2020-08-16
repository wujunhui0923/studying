#!usr/bin/python
#-*- coding = utf-8 -*-


# class Calculation(object):
#     pass


# class Calculation:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def add(self):
#         return self.a + self.b
#
#     def minus(self):
#         return self.a - self.b
#
#     def mulit(self):
#         return self.a * self.b
#
#     def division(self):
#         try:
#             return self.a / self.b
#         except ZeroDivisionError:
#             print("b不能为0")
#
#
# cal = Calculation(2, 0)
# cal.division()

#
# class Phone:
#
#     # 如果不自己定义__init__函数，系统会自动定义的
#     def __init__(self, model, color):
#         self.color = color
#         self.model = model
#
#     def call(self, record=True):
#         if record == True:
#             self.record()
#         print("正在打电话")
#
#     def record(self):
#         print("{}正在录音".format(self))
#
#     def __repr__(self):
#         return self.model
#
#
# iphone = Phone("iphone 8", "黄色")
# # iphone.record()
# iphone.call(False)

"""
1.类和对象
2.类和对象的使用
3.属性，类属性，实例属性，类属性
4.方法：实例方法、类方法、静态方法

类的继承
1.功能机，智能机
2. 如何继承
class 类名（父类名）：
继承以后，子类可以使用父类的所有方法
如果父类和子类具有共同的方法和属性，优先使用子类的属性。---重写



"""

#
# class Phone:
#
#     def call(self):
#         print("正在打电话")
#
#     recharge = True
#
#     def send_msg(self):
#         print("发送短信")
#
#
# class SmartPhone(Phone):
#
#     # def call(self):
#     #     print("正在通话")
#     #
#     # def send_msg(self):
#     #     print("发送短信")
#
#     def caputure_video(self):
#         print("正在视频")
#
#
# smart = SmartPhone()
# smart.call()
# print(smart.recharge)


"""
多重继承
子类可以同时继承多个父类的类和方法
class 类名（父类1，父类2，父类3）
类名：    类名（）:     类名（object）:
所有的类都是继承Object的类，object 的子类


继承父类的问题，当所有的父类中存在相同的父类，先找自己的类中是否存在方法，然后
根据其他父类的顺序进行展示的。


菱形问题，钻石问题，

"""


# class Game_player():
#     def play_games(self):
#         print("正在玩游戏")
#
#
# class MusicPlayer():
#     def play(self):
#         print("正在播放音乐")
#
#
# class Phone:
#
#     def call(self):
#         print("正在打电话")
#
#     recharge = True
#
#     def send_msg(self):
#         print("发送短信")
#
#
# class SmartPhone(Phone, MusicPlayer, Game_player):
#     # def call(self):
#     #     print("正在通话")
#     #
#     # def send_msg(self):
#     #     print("发送短信")
#
#     def caputure_video(self):
#         print("正在视频")
#
#
# smart = SmartPhone()
# smart.call()
# smart.recharge
# smart.play_games()


"""
菱形问题/钻石问题
如果所有的父类中具有相同的方法，
继承顺序的问题：
1，自己2，根据代码当中继承父类的先后顺序查找。
广度优先：
深度优先：
C3算法


"""


class A:
    def play(self):
        print("a is playing")


class B(A):
    def play(self):
        print("b is playing")


class C(A):
    def play(self):
        print("c is playing")


class D(B, C):

    # def play(self):
    #     print("d is playing")
    pass


d = D()
d.play()
# 查找顺序
print(D.__mro__)

"""
超继承
super()  调用父类的方法

"""

"""
debug模式，，
打断点，调试  
step over  F8,下一步，单步调试


step into




"""
"""
接口
什么是接口
前后端沟通的桥梁，系统与系统之间的交互的需要
数据通道
web API 
API:应用程序可编程接口：application programming interface


硬件接口
1. usb
2.水龙头
软件接口
1.用户界面   UI，user interface
web api


http 请求
请求首行
请求头：user-Agent  用户代理
content-type  请求数据格式

请求体
请求方法：put\post\get\delete\copy\head\options\
远程ip地址：
版本号：
域名地址：
IP：HTTP：TCP/IP，，域名和IP的对应关系，，，DNS解析



get,,获取资源   post  发送资源
body:数据传输方式

text    text/plain
Form    application/x-www-form-urlencoded
json    application.json
File    不确定


cookie   让无状态的变更有状态的

HTTP 无状态协议





"""
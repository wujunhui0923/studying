#!usr/bin/python
#-*- coding = utf-8 -*-


"""
1.什么是类；
何轩是什么类：什么种类：人类、大佬类、
同样的一个人，可以属于
共同特征的某一些事务的种类或集合
 表示方法：
#  class 类名（）：
类名也是标识符，由字母、数字、下划线组成的，且不能由数字开头，且不可以是关键字
 大驼峰的命名方式，
 表示方法：


 2.什么是对象
对象就是类当中的某一个成员
TODO：如何表示一个成员


"""
class BigBoss:
    pass
# 类的使用，类的实例化、类的对象化、类的初始化
# 可以使用整个类
print(BigBoss)
# 使用类当中的一个对象、实例
print(BigBoss())
"""
类的属性：包含类属性和实例属性
类属性：类集体的属性

类属性：成员都具备的特征，又称为类变量
类里面表示的变量，就是属性
类属性的修改
类名.属性值 = 新的属性值




实例属性，实例变量
类成员自己独有的属性 

如何定义一个具体的对象
如何去使用对象，初始化一个对象出来，迹象

TODO：初始化对象定义的时候，__init__(self,,)
初始化对象使用的时候其实是调用__init__(self,,)

实例属性如何表示
实例属性的定义：__init__里面self.属性名 = 属性值
实例属性如何使用：实例名称（不是类名），属性名
实例属性的修改，实例名称.属性名 = new 属性值
self:表示在类胡定义当中实例自己

 
"""
# class BigBoss:
#     # 类属性
#     code= "goog"
#     hair = "thin"
#     hobby = "宅"
# print(BigBoss.code)
# print(BigBoss.hair)
# print(BigBoss.hobby)
#
# BigBoss.hobby = "2"
# print(BigBoss.hobby)
#
#
# def __init__(self, name, food ):
#
#     """
#     定义具体的对象，初始化函数，初始化方法
#     :param self:
#     :return:
#     """
#     print(name)
#     print(food)
#     self.Bigdalao_name_name = name
#     pass

# 方法：类里面的函数就是方法
# 函数和方法
# 方法肯属性的关系
# 属性：特征，n.
# 方法：行为、动作，动词

# 方法和方法之间的相互调用
# 没有self的方法：
# 1.静态方法
# 就是表示刚刚好放到类下面的普通函数
# 只是为了方便管理
# 静态方法的调用，

class DaLao:
    def __init__(self, name):
        self.name = name
    @staticmethod
    def eat( food):
        return "大佬喜欢吃{}".format(food)
    def offer(self,money, food):
        print("恭喜{}拿到了{}的offer")
        self.eat(food)
    # 类方法的调用，cls   类本身


    @classmethod

    def code(cls):
        dalao = DaLao('四叶草')
        print("我喜欢的编程语言是{}",format(cls.favor))
        pass

# 类方法：常用来用作构造函数
# 实例方法，用的最多
# 静态方法，有提示的时候需要用


# 什么是方法：类下面的函数，或表示类或者对象的行为
# 方法和方法之间的调用
#
#

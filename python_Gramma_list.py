# #!usr/bin/python
# #-*- coding = utf-8 -*-
# # 数据类型之list、dict;
# # 一、列表的操作
# # 长度  len()
# # 索引和切片，和字符串一样
# # 查找：index()
# # 统计：count
# # 不可变类型，不可以做增删改
# # info = ["yueze",18,"男","矮穷挫",["gao","fu","shuai"],True,"NOne","好的"]
# # 删除列表中的字符
# # info.remove("男")
# # info.pop(2)-----根据索引进行删除操作
# # del info[2]
# # 添加数据
# # user_info.append()
# # user_info.extend()
# # user_info.insert()
# # 修改
# # # user_info[index]="value"
# #
# # # 字典--dict  存储多个数据，多用于获取单个数据
# # # 列表--list  存储多个数据，获取单个元素可读性不强
# # info = {"name":"xiaowang","age":19,"sexy":"女"}
# # key =info["age"]
# # print(key)
# # # key、value,不可变类型，唯一的，，字符串作为key值
# # # 长度
# # print(len(info))
# # # 字典是无序的数据类型，，list是有序的
# #key值是唯一的，且不可变，value值随意
# # 字典是可变类型
# # # 添加元素
# # info["star"]=["周杰伦"]
# # print(info)
# # # 元素修改
#
#
# # 字典中的单引号和双引号没有区别的
# # 删除元素
# # info.popitem()--删除随意的元素
# # print(info)
# # 删除指定的值
# # info.pop(star)
# # info.clear()
# # print(info)
#
#
# # print(info.items())----将键和值进行绑定在一起
# # print(info.keys())---
# # print(info.values())
# #
# # 总结：
# # 字典是无序的，可变的，keys值是唯一的，values随意，items();keys();values();
# # python 3.7以后的版本是内部排序的，你添加的元素显示在最后面，
# # remove返回的是None，
#
# # 字典是无序的，可变类型
# # key是唯一的，values 随意
# # 元祖：小括号
# # 列表：中括号
# # 获取某一个元素，索引
# # 获取多个元素，切片
# # 元祖不可变，不可以进行修改、删除、
# # 元祖的不可变是相对的，不是绝对的，可以修改列表中的值
# # tuple_demo = ()--表示空元祖
# # print(tuple_demo)
# # # 当元祖中仅存在一个值的时候，字符类型为去掉括号后的类型
# # tuple_demo2 = (1)
#
# # 集合表示
# # 可以存储多种类型，{"a",1}
# # 长度len()
# # 集合不是序列，没有顺序，又没有key,没有索引和切片，和字符串一样
# #打印元祖类型type()
# # 1个元素的集合如何表示
# #
# #
# # 序列类型：
# # 字符串、元祖、列表、
# # # TODO：表示一个元素的元祖，可以在元素后面加上一个逗号
# # 元祖解包：
# """
# (11)----整型
# {11，22}---集合，可变类型
# （[11,22,33]）----列表，可变类型
# {"aa":111}---字典，可变类型
#
#
# lis= [11,22,11,33,44,55,22,55,66,88,00]
# 去重：
# li=list(set(lis))
# li_new.sort()
# li_new.pop(-1)
# li_new.pop(-1)
# li_new.remove(11)
# index_11 = li_new.index(77)
# """
# #
# # python 的运算符号
# if....elif ....else
# a = 1


# 数据运算
# 算术运算，加减乘除
# + 、-
# *、/
# // 整除
# %--取余
# **--幂运算
# #TODO：浮点数运算，不能精准
# #
# #
# from decimal import Decimal
# print(Decimal("100.00")-Decimal("0.8") == Decimal("99.2"))
# # Decimal --十进制，接受的是字符串
#
# 赋值运算
name = "xiaozhang"
name +="wang"
name =name +1
print(name)
age = 19
age -= 1
# age = age -1
print(age)

# 比较运算
# > 、<、 == 、!=、 >=、 <=
# False比较预算得到的是布尔值，True/










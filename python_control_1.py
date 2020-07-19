#!usr/bin/python
#-*- coding = utf-8 -*-
# datetime:20200716
# email:15001989175@163.com
# author:wu jun hui
# copyright:
# 将输入的内容转换成整形
# price = int(input("金额："))
# # price_after = price
# if 50<=price <= 100:
#     price_after = price*(1-0.1)
# elif price >100:
#     price_atfer = price*(1-0.2)
# else:
#     price_after = price
# print(price_after)
# 判断是否为闰年：
"""
if 条件中存在多个判断条件的写法：需要括号括起来
    if 和elif、else 后面的冒号需要是英文的
year = 2019
year =input("输入年份")
if ((year % 4 ==0 and year%100 != 0) or (year % 400 ==0)):

    print("该年为闰年")
else:
    print("该年不是闰年")
    """
"""
导入 random
import random
while True:
# input的输出的是字符串
# 自己出拳
# 电脑出拳
# 自己出拳等于4
# 如果电脑出拳和自己的相同--平局
# 如果电脑出拳为石头（自己布）、
电脑出拳为布（自己剪刀）、电脑出拳为剪刀（自己石头）则我赢了
# 否则：我输入了
    choice = input("请输入出拳：（1）石头、（2）剪刀、（3）布、（4）退出")
    
if choice =="4":
    print("退出程序")
    break
# 电脑出拳
    computer_choice =random.randint(1,3)
    if (computer_choice==1 and choice =="3")or (
        computer_choice==2 and choice =="1") or (
        computer_choice==3 and choice =="2"):
        print("我赢了")
    # 字符类型不同的需要进行转换的
    elif str(computer_choice) ==choice:
        print("平局")
    else：
        print("失败")
"""
# 求最大值---
# 定义最大值为变量，和已有的数进行比较
# a = int(input("输入第一个数:"))
# b = int(input("输入第二个数:"))
# c = int(input("输入第三个数:"))
# max_num = a
# if a < b:
#     max_num = b
# if c > max_num:
#    max_num = c
# print(max_num)
# ************列表的排序 ASIII 编码，需要转换的,,,,,,,,,,,可用于多个数据间求最大值
# a = int(input("输入第一个数:"))
# b = int(input("输入第二个数:"))
# c = int(input("输入第三个数:"))
# my_list = [a,b,c]
# my_list.sort()
# print(my_list[-1])

# 求最大值--函数max()--列表中的最大值
# a = int(input("输入第一个数:"))
# b = int(input("输入第二个数:"))
# c = int(input("输入第三个数:"))
# max_num = [a,b,c]
# print(max(a,b,c))
# print(max(max_num))
#利用for 循环求最大值
# a = int(input("输入第一个数:"))
# b = int(input("输入第二个数:"))
# c = int(input("输入第三个数:"))
# my_list_num = [a,b,c]
# max_num=my_list_num[1]
# for i in my_list_num:
#     if max_num< i:
#         max_num = i
# print(max_num)



# 九九乘法表
# for i in range(1,10):
#     for j in range(1,10):
#         if j<=i:
#             print("{}*{}={}".format(i,j,i*j),end="\t")
#     print()
"""
从微信中删除黑名单中的几个人员black_list = ["卖手机","卖保健品","卖面膜","卖化妆品","卖白酒"]
"""
black_list = ["卖手机","卖保健品","卖面膜","卖化妆品","卖白酒"]
# black_list.clear()
# while len(black_list) > 0:
#     black_list.pop(0)
# print(black_list)
# for wx in black_list[:]:
#     black_list.remove(wx)
# print(black_list)
# 总结：for循环中修改列表，，不要在for循环中修改列表，如果要修改，需要进行复制的。。。copy或切片复制[:]
# for i in range(len(black_list)):
#     black_list.pop(0)
# print(black_list)
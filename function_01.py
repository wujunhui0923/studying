#!usr/bin/python
#-*- coding = utf-8 -*-
# 函数：输入（参数）、返回值
# def add(x):
#     y = x+1
#     return y   # 返回的值
# add(2)
# result= add(2)
# print(result)
# print:将某一个值进行打印到屏幕上
# return :函数定义拉出来的东西，使用变量去接收函数的返回值；
# print(add(3))
#函数参数可以是任意类型
"""
def 函数名称(参数1,参数2，参数3)：
    （缩进）函数体
    函数体里面的内容外面无法看到，需要麻烦用变量接收才可以的
    外面能看到的（函数名、参数值（输入），返回值（输出））
    return 返回值。返回值可以有多个的
"""
# 返回多个值的情况：
# def list(x,y):

"""交换值、
    :param x:
    :param y:
    :return:
"""
#     a = x +23
#     # return a,y
#     return {"m":a,"n":y}
# print(list(2,4))

# 函数：存储一段可以重复使用的程序，程序更简洁，可以重复使用
# 代码具有可读性，看函数名称和注释就可以知道作用的。

#     print("""*****************""")
#     print("""姓名:{}""".format(name))
#     print("""年龄:{}""".format(age))
#     print("""性别:{}""".format(sex))
#     print("""*****************""")


# def user_info(name,age,sex):
#     """名片"""
#     print("""*****************""")
#     print("""姓名:{}""".format(name))
#     print("""年龄:{}""".format(age))
#     print("""性别:{}""".format(sex))
#     print("""copyright""")
#     print("""*****************""")
#     # return None  省略
#
#
#
# # fact_name = "yuze"
# # fact_age = 34
# # fact_sex = "男"
# # user_info(fact_name,fact_age,fact_sex)
# #
# # my_list = [1,3]
# # b = my_list.append('hello')
# # c = my_list.pop(1)
# # print(b)
# # print(c)
# # yuze = user_info(fact_name,fact_age,fact_sex)
# # print(yuze)
#
# # 函数定义的参数和实际调用的参数数量相等，顺序相同
# # 函数定义的参数，形式参数--形参，x、y、z
# # 函数调用的参数，实际参数，实际的值，实参，1、2、3
#
# # TODO:1.什么是函数，函数的定义，函数体内的内容，仅有当函数被调用的时候才会被执行
# # 函数的作用   return
# def dalao(name):
#     new_name = "DALAO" + name
#     return new_name
#     print("连长好牛逼")
#     # 函数遇到return 便会终止，不会继续运行
#     # 函数定义后需要调用才能执行里面的逻辑
#
#
# new = dalao("连长")
# print(new)
# def get_bmi(height):
#     if height >= 185:
#         return("高富帅")
#     else:
#         pass
#     print("不是高富帅")
#     if height < 80:
#         return("有点矮")
#     print("普通人")
#     return("小矮人")
# print(get_bmi(10))
# def dalao(name,money,food):
#     print("恭喜{}拿到了一个{}的offer".format(name,money))
#     return()
# dalao("lianzhang","90","")
# 形式参数需要和实际参数保持一致
# 位置参数 形式参数的位置和实际参数的位置需要保持一致，postion
# 关键参数--贴标签,实际是给参数进行赋值，可以进行顺序调换，
# 可以部分作为关键字参数，TODO：先定义位置参数，后定义关键字参数
# 默认参数--可以少传参数
# dalao(name ="lianzhang",money ="90",food="")

# def dalao(name,money,food="橘子"):
#     print("{}喜欢吃{}".format(name,food))
#     return
# 默认参数需要放到位置参数胡后面，默认参数可以不传值

# dalao("蛋蛋","20K","鸡腿")
# dalao("蛋蛋","20K")





# 不定长参数，
# 在函数定义里面，可以用*args去接收多余的参数
# 在函数定义里面，args 是元祖
# def sum(a,b,*args):
#     """*args 表示剩下多余的参数"""
#     print(args)
#     total = 0
#     c = total +a +b
#     for i in args:
#         c += i
#     return c
# 在函数的调用中，也可以用*value
# 可以是列表，可以是元祖

# rest = [1,4,6]
# print(sum(3,4,*rest))

#
# def sum(a,b):
#     total = 0
#     c =total+a+b
#     return c
# def sum_total(a,b,*args,**kwargs):
#     """**kwargs表示接收多余的关键字参数"""
#     print(args)
#     print(kwargs)
# #     函数体里面胡kwargs是字典的形式接收多余胡关键字参数
#
#
# other_info ={"hobby":"girl","food":"苹果"}
# # hobby ="girl",food = "苹果"
# sum_total(3,4,name="dandna",age=22,hobby="girl")

# 函数的返回值return,

#函数的作用域
#
#
# def main():
#     name = "深海的鱼"
#     offer = "40K"
#     dalao(name,offer)
# def dalao(name,money,food="鸡腿"):
#     print("{}拿到了{}offer".format(name,money))
#     eat(name,food)
#     return
# def eat(dalaoname,food):
#     print("{}最喜欢吃{}".format(dalaoname,food))
#     return
# main()


""" 函数体内的变量为局部变量，函数体外的变量为全局变量，，局部变量仅可以在函数体内
使用，不可以在函数体外使用
全局变量可以在函数体内使用的
"""
# name = "hexuan"
# def gaoshou():
#     name = "dandan"
#     print("{}是一个绝世高手".format(name))
#     return
#
#
# gaoshou()
# id(),查看某个值或变量在内存中的地址,函数的参数是局部变量
# 全局变量和局部变量的修改
#
# 局部变量可以在函数体中进行修改--可以修改
# 局部变量能在函数体外面被修改吗---不能修改，无法获取
# 全局变量可以在函数体中修改吗？--不可以修改
# global全局变量，但不建议使用前期




# 内置函数：
# python 自己定义的函数 print(),input(),len(),type(),max(),help(),min(),
# eval()--脱字符串衣服，sum(),zip()

# 模块导入：
# 什么是模块--就是一个Python文件--，module
# 包，package
# 模块导入的作用
# 库：标准库，第三方，实现特定功能的代码集合，一个模块，一个包


# 函数的相互调用，
# 局部变量、全局变量
# 修改
# 常用的内置函数
# 查看源码的方法：
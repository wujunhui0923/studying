#!usr/bin/python
#-*- coding = utf-8 -*-
"""
模块：
包：
1.模块名称--标识符
a.数字、下划线、字母，不能以数字开头，不能是关键字
模块名称一般是下划线的形式命名的，
模块名称不能和python 中的内置模块名称重合，
random、time--内置模块，在命名内置模块的时候不可以使用的

"""
"""
2.模块导入
from 模块名称.import .类名、函数名、变量名.，适用于项目根目录/内置模块
"""


# from time import time
# print(time())
# from random import randint
# # randint 是函数名称
# print(randint(1,88))

# from modle_1 import run
# print(run())

# from (项目的根目录开始)包名.包名.模块名  import  类名、函数名、内置模块
# from (项目的根目录开始)包名.包名.模块名  import 模块名
# 使用的时候，模块名.函数名
#  如果出现函数名称相同的情况，需要取别名

# import 模块名 as，避免名称过长，避免和其他名称重复
# 其中使用import 时仅可以使用模块名称
# 函数调用：模块名称.函数名()
# import 包名.包名.模块名
# # 执行导入时，所有顶格的内容
# """
# __file__   :这个是模块的路径
# __name__   :表示运行python 文件的模块名
# """
# 如果想直接执行某个python 文件，自己定义好的函数或则类使用
# if __name__ == '__main__':用于调试用的
#     print("一切正常")

# from 包名 import *（通配符）
# 容易导致名称重复，引起冲突


"""
OS 模块是别人写好的，python 内置的
如果不是python 内置的，放到项目下面，作为一个包或模块
主要处理系统相关的
os.path 

"""
# import os
# # pwd 显示当前文件路径,匀
# print(os.getcwd())
#
# print(os.path.abspath(__file__))
# 获取绝对路径
# a=os.path.dirname(os.path.abspath(__file__))
# print(os.path.dirname(os.path.abspath(__file__)))
# # 路径拼接   os.path.join()
# # print(os.path.join("a","yuze.txt"))
# # 创建文件夹一次仅能创建一个文件夹
# data_path =os.path.join(a,"data")
# os.mkdir(data_path)
#
# # 判断是否是一个文件夹
# print(os.path.isdir(data_path))
# # 判断是否是一个文件
# print(os.path.isfile(data_path))

# 判断路径是否存在
# print(os.path.exists(data_path))


# os,open 的作用，自动生成报告

# 如何读取文件
# 1.打开文件，内置函数open()
# 2.open(path/文件名称)--绝对路径
# 3.关闭文件--一定需要关闭文件的。文件丢失或无法正常打开
# 根据指定的编码格式读取------解码
# mode  r--读，w---写入  a--追加
# import os
# dir_name =os.path.dirname(os.path.abspath(__file__))
# ceshiwenjian = os.path.join(dir_name, "ceshiwenjian.txt")
# f = open(ceshiwenjian,encoding='utf-8')
# print(f.read())
# f.close()
#
# # 文件写入
# f= open(ceshiwenjian, mode='w', encoding='utf-8')
# f.write('快乐学python')
# f.close()
#
#
# f= open(ceshiwenjian, mode='a', encoding='utf-8')
# f.write('快n')
# f.close()



#  b
# readline ----仅读取一行
#
# import os
# dir_name =os.path.dirname(os.path.abspath(__file__))
# ceshiwenjian = os.path.join(dir_name, "ceshiwenjian.txt")
# f = open(ceshiwenjian,encoding='utf-8')
# # while True:
#     line =f.readline()
#     if not line:
#         break
#     print(line)
# a = f.readlines()
# for i in a:
#     print(i, end="")


# 异常处理,一旦程序报错，程序便会终止运行
num1 = input("请输入数字1：")
num2 = input("请输入数字2：")
try:
    print(num1*num2)

except TypeError:
    print("继续运营")
except IndexError:
    print("继续32323运营")

# 异常类型：
# importError
# NameError
# IndexError
# TypeError
# keyError
# SyntaxError--语法错误

# 不适用默认的捕获异常，一般可以使用异常类型
# 总结：os模块，open(),try,except--异常捕获


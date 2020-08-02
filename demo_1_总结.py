#!usr/bin/python
#-*- coding = utf-8 -*-

# 相对路径和绝对路径--os.path.abspath(__file__                                           )
# 绝对路径，每次都需要从最开始的地方查找
# 相对路径：依据现有的路径查找
# import os
# path_name = os.path.dirname(os.path.abspath(__file__))
# print(path_name)
# root_path = os.path.dirname(path_name)
# print(root_path)
# # 判断文件是否存在，如果不存在就创建
# if not os.path.exists(path_name):
#     os.mkdir(path_name)

# 文件读写：
# f = open(file_path, mode="r", encoding="utf-8")
# f.read()  # 读取文件，根据光标读取   seek()

# f.readlines()  # 列表
# f.close()   # 关闭文件
# 既想读取，又想写入，w+，，，r+
# path_name = os.path.join(path_name, "lianzhang.txt")
# f= open(path_name, "w+", encoding="utf-8")
# f.write('lianzhang is dalao')
# f.close()
# f = open(path_name, 'r',encoding='utf-8')
# # f.seek(0),移动光标
# print("读取", f.read())
# f.close()



# 3.异常处理
# try:
#     # 执行
# except Exception as r:  # 通用的；具体的， TypeError
#     print(r)
# except NameError as y:
#     print()
#     raise KeyError

# finally:
# #     不管有没有报错，程序是否正常执行，都会执行的语句
#     print("这是可以正常处理的")
# with open(path_name, "w+", encoding= "utf-8") as a:
#     a.write('很好')


# def add(a, b):
#     if not isinstance(a, int):
#         raise ValueError
#     return (a+b)
#
#
# print(add(7,4))



















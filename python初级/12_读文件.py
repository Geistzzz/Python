# -*- coding = utf-8 -*-
# @Time : 2024/3/16 20:45
# @Author : Geist
# @File ： 12_读文件.py
# @Software: PyCharm
import base64

# utf编码相关
# name = '张驰'
# data = name.encode('utf-8')
# data = data.decode('utf-8')
# print(data)

# 文件打开三步骤

# 打开文件
file_object = open('/Users/mac/Documents/Python/python初级/info.text', mode='rb')

# 读取文件
data = file_object.read()

# 将字节解码
data1 = data.decode('gbk')
data2 = data.decode('utf-8')

# 打印
print(data1)  # 字节类型
print(data2)

# 优化后的打开文件的方式

file_object = open('/Users/mac/Documents/Python/python初级/info.text', mode='rt', encoding='utf-8')
print(file_object.read())

# 关闭文件
file_object.close()
# os模块的使用
import os

file_path = 'test.txt'
if not os.path.exists(file_path):
    print('文件不存在')

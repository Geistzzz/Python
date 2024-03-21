# -*- coding = utf-8 -*-
# @Time : 2024/3/16 21:35
# @Author : Geist
# @File ： 13_写文件.py
# @Software: PyCharm

# 第一步打开文件

file_object = open('../python脚本开发/t1.txt', mode='wb')

# 写入内容
file_object.write('hello world'.encode('utf-8'))

# 关闭文件
file_object.close()

# 优化后的写文件方式
file_object = open('../data/t2.txt', mode='wt')

# 写入内容
file_object.write('张驰')

# 关闭文件
file_object.close()

# 打开图片
photo_object = open('../data/t3.jpeg', mode='rb')
# 读取图片内容
b_object = photo_object.read()
# 关闭图片
photo_object.close()

# 打开图片
photo_object = open('../data/t4.jpeg', mode='wb')
# 写入内容
photo_object.write(b_object)
# 关闭文件
photo_object.close()


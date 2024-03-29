# -*- coding = utf-8 -*-
# @Time : 2024/3/17 00:21
# @Author : Geist
# @File ： 15_文件路径.py
# @Software: PyCharm

# 获取当前工作目录路径
# import os
# 获取当前工作目录的三种方法
# os.path.dirname(__file__)
# print(os.getcwd())  # 获取当前工作目录路径
# print(os.path.abspath('.'))  # 获取当前工作目录路径
#
# weight_path = '/weights.txt'
# current_work_dir = os.path.dirname(__file__)  # 当前文件所在的目录
#
# weight_path = os.path.join(current_work_dir, weight_path)  # 再加上它的相对路径，这样可以动态生成绝对路径
#
# print(weight_path)

# 创建文件夹

import os

# 操作的文件夹路径

operate_path = r"/Users/mac/Documents/Rustproject"
for root, dirs, files in os.walk(operate_path):
    print('root:', root)
    print('dirs:', dirs)
    print('files:', files)
    print('\n')

pathtest = "/Users/mac/Documents/Python/python初级/15_文件路径.py"

path = os.path.join(path, exchange.id)
if os.path.exists(path) is False:
    os.mkdir(path)

    # 获取所有文件路径
    symbol_file_path = glob(kline_path + '*USDT.csv')  # 获取kline_path路径下，所有以usdt.csv结尾的文件路径

# mac/linux的文件路径和windows的文件路径有什么不同
# 在类 Unix（例如 Linux 和 macOS）系统中，文件路径使用正斜杠（/）作为目录分隔符。
# 在 Windows 系统中，文件路径使用反斜杠（\）作为目录分隔符。


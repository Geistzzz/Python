# -*- coding = utf-8 -*-
# @Time : 2024/3/18 22:23
# @Author : Geist
# @File ： 键盘操作.py
# @Software: PyCharm

from pynput.keyboard import Key, Controller

keyboard = Controller()

# shift 有两个键，一个是左边的、一个是右边的，此时相当于输入感叹号

with keyboard.pressed(Key.shift_l):
    keyboard.press("！")
    keyboard.release("！")

# # 如果要同时按下多个键，那就输入多个键即可
# with keyboard.pressed(Key.shift_l, Key.ctrl_l):
#     keyboard.press(Key.f10)

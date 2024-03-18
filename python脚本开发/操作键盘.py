# -*- coding = utf-8 -*-
# @Time : 2024/3/18 22:16
# @Author : Geist
# @File ： 操作键盘.py
# @Software: PyCharm


from pynput.keyboard import Key, Controller

# 实例化一个可以操作键盘的对象
keyboard = Controller()

# 按下 a 键，小写
# keyboard.press("a")
# # 松开 a 键
# keyboard.release("a")

# 按下 A 键，大写
# for i in "hello":
#     keyboard.press(i)
#     # 松开 A 键
#     keyboard.release(i)
# """
# 像英文字符、数字等等直接输入相应的字符即可
# 但如果是 shift、ctrl 等键，那么需要调用 Key 里面属性xxx

# 按下大写键dd
keyboard.press(Key.caps_lock)
# 松开大写键
keyboard.release(Key.caps_lock)

# -*- coding = utf-8 -*-
# @Time : 2024/2/28 10:48 下午
# @Author : 张驰
# @File ： test.py
# @Software: PyCharm

import pyautogui


# print(pyautogui.size())
# print(pyautogui.position())

sizex,sizey=pyautogui.size()
# print(sizex,sizey)

pyautogui.moveTo(sizex/2,sizey/2,duration=90)


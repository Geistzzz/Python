# -*- coding = utf-8 -*-
# @Time : 2024/3/18 22:33
# @Author : Geist
# @File ： 键盘监控.py
# @Software: PyCharm

from pynput.keyboard import Key, Listener

def on_press(key):
    # 当按下esc，结束监听
    if key == Key.esc:
        print(f"你按下了 esc，监听结束")
        return False
    print(f"你按下了 {key} 键")

def on_release(key):
    print(f"你松开了 {key} 键")


with Listener(
    on_press=on_press,
    on_release=on_release
) as listener:
    listener.join()
"""
你按下了 'a' 键
你松开了 'a' 键
你按下了 Key.backspace 键
你松开了 Key.backspace 键
你按下了 Key.shift 键
你松开了 Key.shift 键
你按下了 'c' 键
你松开了 'c' 键
你按下了 Key.enter 键
你松开了 Key.enter 键
你按下了 esc，监听结束
"""

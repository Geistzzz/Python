# -*- coding = utf-8 -*-
# @Time : 2024/3/18 22:09
# @Author : Geist
# @File ： 监控鼠标.py
# @Software: PyCharm

from pynput.mouse import Listener, Button


def on_move(x, y):
    print(f"鼠标移动到: ({x}, {y})")


def on_click(x, y, button, is_press):
    if button == Button.left:
        button = "左键"
    else:
        button = "右键"
    if is_press:
        operator = "按下"
    else:
        operator = "松开"

    print(f"鼠标{button}在 ({x}, {y}) 处{operator}")


def on_scroll(x, y, dx, dy):
    if dx:
        print(f"滑轮在 ({x}, {y}) 处向{'右' if dx > 0 else '左'}滑")
    else:
        print(f"滑轮在 ({x}, {y}) 处向{'下' if dy > 0 else '上'}滑")


with Listener(on_move=on_move,on_click=on_click,on_scroll=on_scroll) as listener:
    listener.join()

"""
鼠标移动到: (783.17578125, 302.7890625)
鼠标移动到: (777.2734375, 302.7890625)
鼠标移动到: (769.5703125, 302.7890625)
鼠标移动到: (758.74609375, 302.7890625)
滑轮在 (111.03515625, 609.31640625) 处向上滑
滑轮在 (111.03515625, 609.31640625) 处向上滑
滑轮在 (111.03515625, 609.31640625) 处向上滑
滑轮在 (111.03515625, 609.31640625) 处向左滑
滑轮在 (111.03515625, 609.31640625) 处向左滑
鼠标左键在 (649.44140625, 448.4765625) 处按下
鼠标左键在 (649.44140625, 448.4765625) 处松开
"""

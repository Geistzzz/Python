# -*- coding = utf-8 -*-
# @Time : 2024/3/18 22:12
# @Author : Geist
# @File ： 阻塞.py
# @Software: PyCharm


from pynput.mouse import Listener, Button

def on_click(x, y, button, is_press):
    if button == Button.right:
        print("点击鼠标右键，监听结束")
        return False
    if is_press:
        operator = "按下"
    else:
        operator = "松开"

    print(f"鼠标左键在 ({x}, {y}) 处{operator}")


with Listener(
    on_click=on_click,
) as listener:
    listener.join()
"""
鼠标左键在 (28.453125, 610.71484375) 处按下
鼠标左键在 (28.453125, 610.71484375) 处松开
点击鼠标右键，监听结束
"""

listener = Listener(
    on_move=on_move,
    on_click=on_click,
    on_scroll=on_scroll)

# 启动子线程开启监听，主线程会继续向下执行
listener.start()
# 如果不想监听了，可以调用 stop 方法结束
listener.stop()
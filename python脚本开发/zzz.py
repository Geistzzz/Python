# -*- coding = utf-8 -*-
# @Time : 2024/3/18 22:13
# @Author : Geist
# @File ： zzz.py
# @Software: PyCharm

from pynput.mouse import Listener, Button
listener = Listener(
    on_move=on_move,
    on_click=on_click,
    on_scroll=on_scroll)

# 启动子线程开启监听，主线程会继续向下执行
listener.start()
# 如果不想监听了，可以调用 stop 方法结束
listener.stop()

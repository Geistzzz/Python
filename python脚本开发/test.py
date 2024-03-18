# -*- coding = utf-8 -*-
# @Time : 2024/3/18 22:03
# @Author : Geist
# @File ： test.py
# @Software: PyCharm

from pynput.mouse import Button, Controller

# 实例化 Controller 得到一个可以操作鼠标的对象
mouse = Controller()
# mouse.position: 获取当前鼠标位置。
# 屏幕左上角坐标为 (0, 0)，右下角为 (屏幕宽度, 屏幕高度)
print(f"当前鼠标位置: {mouse.position}")
"""
当前鼠标位置: (881, 467)
"""

# 给 mouse.position 赋值等于移动鼠标，这里相当于移动到 (100, 100) 的位置
# 如果坐标小于 0，那么等于 0。如果超出屏幕范围，那么等于最大范围
# mouse.position = (100, 100)  # 此方法等价于 mouse.move(100, 100)
print(f"当前鼠标位置: {mouse.position}")
"""
当前鼠标位置: (100, 100)
"""


# 按下左键, 同理 Button.right 是右键
# mouse.press(Button.left)
# 松开左键
# mouse.release(Button.left)
# 上面两行连在一起等于一次单击
# 如果这两行紧接着再重复一次，那么整体会实现双击的效果
# 因为两次单击是连续执行的，没有等待时间。
# 如果中间来一个 time.sleep，那么就变成两次单击了


# 当然鼠标点击我们有更合适的办法，使用 click 函数
# 该函数接收两个参数：点击鼠标的哪个键、以及点击次数
# 这里连续点击两次，等于双击
# mouse.click(Button.right, 2)

# 垂直方向、沿着 y 轴向下滑动 2 个 step
# 第一个参数针对水平方向，第二个参数针对垂直方向
# 具体的值表示移动的 step 数
# mouse.scroll(0, 50)
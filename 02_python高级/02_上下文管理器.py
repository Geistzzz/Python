# 什么是上下文管理器
# 一个对象
# 定义了运行时的上下文
# 使用with语句

# with open("mydata.txt", "w") as f:
#     f.write("Hello")
import time


class Timer:
    def __init__(self):
        self.elapsed_time = 0

    def __enter__(self):  # timer其实是self
        self.start_time = time.perf_counter()
        return self

    def __exit__(self, type, value, traceback):
        self.stop_time = time.perf_counter()
        self.elapsed_time = time.perf_counter() - self.start_time


with Timer() as timer:
    nums = []
    for n in range(10000):
        nums.append(n ** 2)

print(timer.elapsed_time)

# 开-关
# 锁-释放
# 启动-停止
# 改变-重置

import datetime as dt
from functools import wraps

# 装饰器参考模版
"""
def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        ret = func(*args, **kwargs)
        return ret
    return wrapper
@装饰器名
def my_func():
    pass
    
"""


def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = dt.datetime.now()
        ret = func(*args, **kwargs)
        print(f"{func.__name__}花费的时间为：", dt.datetime.now() - start)
        return ret

    return wrapper


@decorator
def caculate_time():
    a = 0
    for i in range(100000000):
        a += i
    print(a)


# 带参数的装饰器
# 又把装饰器包了一遍，返回一个装饰器函数
def welcome(name):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"{func.__name__},{name}")
            result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator


@welcome("Tom")  # 相当于返回了一个装饰器
def my_fun(message):
    print(message)


if __name__ == '__main__':
    print(caculate_time.__name__)
    my_fun('dddd')

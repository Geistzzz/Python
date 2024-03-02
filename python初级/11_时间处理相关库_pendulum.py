# -*- coding = utf-8 -*-
# @Time : 2024/3/2 1:14 下午
# @Author : 张驰
# @File ： 11_时间处理相关库_pendulum.py
# @Software: PyCharm

import pendulum as pd

# 获取当前时间
now = pd.now()
print(now.tz)


# 时间转字符串
print(now.to_datetime_string())  # datetime
print(type(now.to_datetime_string())) # str
print('datetime:', now.day)  # datetime
print(now.to_day_datetime_string())  # day
print(now.to_date_string())  # only date

# 字符串转时间 # 指定时区
print(pd.parse('2024-03-02 13:22:57', tz='Asia/Shanghai'))
print(pd.parse(now.to_datetime_string()))

# 时间截取
six_days_ago = now.subtract(days=6)
print(six_days_ago)
list_days = now - six_days_ago
days_list = [i.to_date_string() for i in list_days]
print(days_list)

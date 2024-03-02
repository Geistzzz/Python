# -*- coding = utf-8 -*-
# @Time : 2024/3/1 10:42 下午
# @Author : 张驰
# @File ： 10_Python处理时间.py
# @Software: PyCharm

# import time
#
# t1 = time.time()  # 这个获得的是一个时间戳
#
# time.sleep(1)  # 程序等待1s

# import datetime
#
# # 总揽：获取当前时间的全部信息用这条语句
# # 方法1
# print("---获取当前datetime---")
# current_datetime_1 = datetime.datetime.now()  # 首推
# current_datetime_2 = datetime.datetime.today()
# print(current_datetime_1, current_datetime_2, current_datetime_1 == current_datetime_2)
# # 格式化输出字符串
# print("---格式化输出字符串---")
# print(current_datetime_1.strftime("%Y%m%d%H%M%S"), current_datetime_2.strftime("%Y-%m-%d-%H-%M-%S"),
#       current_datetime_1 == current_datetime_2)
# # 解析字符串成时间格式
# print("---解析字符串成时间格式---")
# test_datetime = "2023-08-09"
# print(type(test_datetime))
# parsed_datetime = datetime.datetime.strptime(test_datetime, "%Y-%m-%d")
# print(type(parsed_datetime))

# # 获取当前年份
# print("---获取当前年份---")
# current_year_1 = datetime.datetime.now().year  # 首推
# current_year_2 = datetime.datetime.today().year
# print(current_year_1, current_year_1, current_year_1 == current_year_2)
# # 获取当前日期：四种方法
# print("---获取当前日期---")
# current_date_1 = datetime.datetime.now().date()  # 首推
# current_date_2 = datetime.date.today()
# current_date_3 = datetime.datetime.date(datetime.datetime.now())
# current_date_4 = datetime.datetime.today().date()
# print(current_date_1, current_date_2, current_date_3, current_date_4,
#       current_date_1 == current_date_2 == current_date_3 == current_date_4)
# # 获取当前月份
# print("---获取当前月份---")
# current_month_1 = datetime.datetime.now().month  # 首推
# current_month_2 = datetime.datetime.today().month
# print(current_month_1, current_month_2, current_month_1 == current_month_2)
# # 获取当前时间
# print("---获取当前时间---")
# current_time_1 = datetime.datetime.now().time()  # 首推
# current_time_2 = datetime.datetime.today().time()
# print(current_time_1, current_time_2, current_time_1 == current_time_2)


# 一种集成的包
import calendar

# 打印一个日历 暂时用不到
# year = 23
# month = 12
# print(calendar.month(year,month))

# current_datetime = dt.datetime.now()
# current_year = current_datetime.year
# current_month = current_datetime.month
# current_weekday = current_datetime.weekday()  # 从0开始
# week_number = current_datetime.isocalendar()[1]  # 一年当中第几周
# curent_dat = current_datetime.day
# print('今年是', current_year, '年', current_month, '月份', '星期', current_weekday, '一年中的第', week_number, '周', '这个月的第',
#       curent_dat, '天')

# # datetime模块里面的date类
# from datetime import date
#
# # 根据时间戳转换日期
# current_time_stamp = time.time()
# print(date.fromtimestamp(current_time_stamp))
# # 生成datetime对象
# print(date(year=2024, month=3, day=2))
# # 时间对象转字符串
# print(date.strftime(date.today(), "%Y%m%d"))
# # 字符串转时间对象

# datetime模块里面的date类
# from datetime import time
# t1 = time(hour=20,minute=58,second=12,microsecond=34455)
# print(t1)

# datetime模块里面的datetime
# from datetime import datetime
# now = datetime.now() # 可以添加时区


# # 时间加减
# import datetime as dt
#
# dt0 = dt.datetime.now()
#
# dt1 = dt0 - dt.timedelta(days=1)
#
# dt2 = dt0 + dt.timedelta(days=1)
#
# # dt3 = dt0 + dt.timedelta(days=1)
#
# print(dt0, dt1, dt2)
#
# timedelta = dt2 - dt0
# print(timedelta.days)
# print(timedelta.seconds)
# print(timedelta.microseconds)
# print(timedelta.total_seconds())  # 换算成秒

# 时区模块


# -*- coding = utf-8 -*-
# @Time : 2024/3/18 23:27
# @Author : Geist
# @File ： Heilum.py
# @Software: PyCharm

from helium import *
from time import sleep

# 简短的测试
# start_chrome("www.baidu.com")
# write("原神")
# press(ENTER)
# kill_browser()

# 点击新闻连接
# start_chrome("www.baidu.com")
# click(Link("新闻"))
#
# sleep(5)
# kill_browser()

# next——test

# start_chrome("www.baidu.com")
# click(Link(to_right_of="新闻"))
#
# sleep(5)
# kill_browser()

# 无界面浏览器
# start_chrome("www.baidu.com",headless=True)

start_firefox("google.com")
start_chrome(headless=True)
from selenium.webdriver import ChromeOptions
#firefox引入FirefoxOptions
options = ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--proxy-server=1.2.3.4:5678')
start_chrome("www.baidu.com",headless=True,options=options)

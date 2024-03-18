# -*- coding = utf-8 -*-
# @Time : 2024/3/19 00:20
# @Author : Geist
# @File ： 脚本开发.py
# @Software: PyCharm


from helium import *
from time import sleep
from selenium.webdriver import ChromeOptions

# options = ChromeOptions()
# options.add_argument('--start-maximized')
start_chrome("www.baidu.com", options=options)
write("原神")
press(ENTER)
click(Link("原神 - 百度百科"))  # 浏览器元素还有button
sleep(5)
# kill_browser()

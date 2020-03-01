# -*- coding: utf-8 -*-
# 作者: 顾名思义
# 时间: 2019/2/13 9:32
# 文件: browsers.py
import os

class Browsers():

    def __init__(self,browserType):
        self.browserType=browserType

    def select_browser(self):

        if self.browserType=='Chrome':
            browser = os.path.abspath('../..') +r'/driver/chromedriver.exe'
            print(browser)
            return browser
        elif self.browserType=='IE':
            pass
        elif self.browserType=='FireFox':
            pass

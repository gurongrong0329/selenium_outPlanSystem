# -*- coding: utf-8 -*-
# 作者: 顾名思义
# 时间: 2018/10/18 13:39
# 文件: test_login.py
import os
import sys
sys.path.append(os.path.abspath('..'))
from selenium import webdriver
from src.pages.login_page import Login
import unittest
from src.common.browsers import Browsers
from config.userinfo import *
from time import sleep



class TestDatetime(unittest.TestCase):

    def setUp(self):
        global driver
        browser = Browsers(browserType)
        self.driver = webdriver.Chrome(browser.select_browser())
        self.user = Login(self.driver)
        self.user.login(address, account, password)

    def test_time(self):
        sleep(5)
        self.driver.get('https://outbound.ynt.ai/outplan/index.html#/callReport')
        sleep(2)
        js="document.getElementsByClassName('ivu-input-wrapper')[0].children[2].value='2020-02-25 - 2020-02-26'"
        # js="$('.ivu-input-wrapper input').value='2020-02-25 - 2020-02-26'"
        self.driver.execute_script(js)
        sleep(5)


    def tearDown(self):
        #登出
        self.user.loginOut(account)
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
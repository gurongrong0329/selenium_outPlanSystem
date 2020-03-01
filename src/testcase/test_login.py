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



class Testlogin(unittest.TestCase):
    driver=None
    check = None
    user=None

    @classmethod
    def setUpClass(cls):
        print('first...')

    @classmethod
    def tearDownClass(cls):
        print('last...')

    def setUp(self):
        global driver
        browser = Browsers(browserType)
        self.driver = webdriver.Chrome(browser.select_browser())
        #self.driver = webdriver.PhantomJS(r'D:\迅雷下载\phantomjs-2.1.1-windows\bin\phantomjs')

    def test_login(self):
        u"""账号登录"""
        global check,user
        user=Login(self.driver)
        user.login(address,account,password)
        # check = AssertFunction()
        # self.assertTrue(check.isElementExist(self.driver,e_personalDetails))
        # self.assertIn('homepage',self.driver.current_url)

    def tearDown(self):
        #登出
        user.loginOut(account)
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
# -*- coding: utf-8 -*-
# 作者: 顾名思义
# 时间: 2018/10/18 11:59
# 文件: login.py
import os
import sys
sys.path.append(os.path.abspath('..'))
import time
from selenium.webdriver.common.action_chains import ActionChains
from config.userinfo import *
# from poium import Page,PageElement
from src.common.locate_element import LocateElement

class Login(LocateElement):

    def __init__(self,driver):
        self.driver=driver
        super().__init__(driver)

    #登录
    def login(self,url,account,password):
        self.driver.get(url)
        self.driver.maximize_window()
        self.by_xpath(e_account).send_keys(account)
        self.by_xpath(e_password).send_keys(password)
        self.by_xpath(e_login_button).click()

    #登出
    def loginOut(self,account):
        time.sleep(5)
        ActionChains(self.driver).move_to_element(self.by_xpath(e_moveAccount.replace('%var%',account))).perform()
        time.sleep(2)
        self.by_xpath(e_loginOut).click()

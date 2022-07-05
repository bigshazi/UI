import os
import time

import pytest as pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from Auto_Test.element.log import GetLogger

mylogger = GetLogger(logger='Test_mylog').get_logger()

class Test_case_search():
    def open_page(self):
        # 切换成H5显示
        mobile_emulation = {'deviceName': 'iPhone X'}
        options = webdriver.ChromeOptions()
        options.add_experimental_option('mobileEmulation', mobile_emulation)
        drivers = webdriver.Chrome(r'D:\Win_TestEngineLite_20210120\chromedriver.exe', chrome_options=options)
        mylogger.info('打开浏览器')
        drivers.implicitly_wait(8)
        drivers.maximize_window()
        drivers.get('https://market.m.taobao.com/app/pm/new-main/home?pha=true&disableNav=YES')
        mylogger.info('打开拍卖首页')
        time.sleep(1)
        mylogger.info('暂停1秒')
        #点击搜索框
        drivers.base_click('//*[@id="root"]/div/div[1]/a[1]')
        #输入关键字
        drivers.base_input('//*[@id="root"]/div/div[1]/form/input','手机')
        drivers.find_element(By.ID,)

case = Test_case_search()
# if __name__ == "__main__":
#     pytest.main()



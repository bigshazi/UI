import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from Auto_Test.element.Basepage import Basepage
from Auto_Test.element.log import GetLogger

mylogger = GetLogger(logger='Test_mylog').get_logger()


class Test_mylog(Basepage):
    """测试"""
    def test_01(self):
        self.showH5() #调用封装的函数
        self.driver.implicitly_wait(8)
        self.driver.get('https://market.m.taobao.com/app/pm/new-main/home?pha=true&disableNav=YES')
        mylogger.info('打开拍卖首页')
        time.sleep(2)
        mylogger.info('暂停2秒')
        self.driver.execute_script("document.body.style.zoom='1'")#解决点击之后屏幕变大问题
        self.base_click("xpath","//a[.='房产']")
        mylogger.info('点击跳转')
        time.sleep(2)
        #截图
        self.base_get_image()
        #去掉新人弹框
        self.base_click('class_name','mask')
        #做个断言，判断新人弹框消失，并截图
        if self.base_element_is_exist == 'false' :
            assert '新人弹框去除'
        time.sleep(1)
        self.base_get_image()
        self.driver.quit()
        mylogger.info('浏览器关闭并推出服务')


testlog = Test_mylog('test')
testlog.test_01()#输出日志


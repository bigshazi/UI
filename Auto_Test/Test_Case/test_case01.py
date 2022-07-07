
import time
import unittest
from Auto_Test.element.Basepage import Basepage
from Auto_Test.element.log import GetLogger

mylogger = GetLogger(logger='Test_case_search').get_logger()

class Test_case_search(unittest.TestCase):
    #前置操作

    def setUp(self):
        self.driver = Basepage('driver') #用于前置引用基础类的方法

    def test_01(self):
        # 切换成H5显示
        self.driver.showH5()
        #打开拍卖页面
        self.driver.base_open_url('https://market.m.taobao.com/app/pm/new-main/home?pha=true&disableNav=YES')
        #等待2秒
        self.driver.base_wait(2)
        #点击搜索框
        self.driver.base_click('xpath','//*[@id="root"]/div/div[1]/a[1]')
        #输入关键字
        self.driver.base_input('xpath','//*[@id="root"]/div/div[1]/form/input','手机')
        time.sleep(2)
        #点击搜索
        self.driver.base_click('xpath','//*[@id="root"]/div/div[1]/div[2]')
        #等待2秒
        time.sleep(2)
        #获取列表文案
        ret = self.driver.base_get_text('xpath','//*[@id="guid-list-3208944720-0"]/div[1]/a/div[2]/div[1]/span')
        #断言列表文案中包含’机‘
        try:
            self.assertIn("机", ret)
            mylogger.info('断言成功')
            time.sleep(2)
            self.driver.base_get_image('断言成功截图')
        except Exception as e :
            mylogger.error('断言失败的原因是{}'.format(e))
            time.sleep(2)
            self.driver.base_get_image('断言失败截图')

            #将失败截图放到html报告中

    def tearDown(self):
        self.driver.base_quit_browser()  # 后置退出浏览器
if __name__ == "__main__":
    unittest.main()



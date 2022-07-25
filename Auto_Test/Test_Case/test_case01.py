import threading
import time
import unittest
from Auto_Test.element.Basepage import Basepage
from Auto_Test.element.log import GetLogger

mylogger = GetLogger(logger='Test_case_search').get_logger()



class Test_case_search(unittest.TestCase):

    #前置操作

    def setUp(self):
        print("每个用例之前执行一次")
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
    def test_02(self):
        self.driver.showH5()  # 调用封装的函数
        self.driver.base_open_url('https://market.m.taobao.com/app/pm/new-main/home?pha=true&disableNav=YES')
        mylogger.info('打开拍卖首页')
        time.sleep(2)
        mylogger.info('暂停2秒')
        self.driver.base_click("xpath", "//a[.='房产']")
        mylogger.info('点击跳转')
        time.sleep(2)
        # 截图
        self.driver.base_get_image("跳转截图")
        # 去掉新人弹框
        self.driver.base_click('class_name', 'mask')
        # 做个断言，判断新人弹框消失，并截图
        if self.driver.base_element_is_exist('class_name', 'mask') == 'false':
            assert '新人弹框去除'
        time.sleep(1)
        self.driver.base_get_image("去除新人弹框")
        # 斷言為全部房源
        ret = self.driver.base_get_text('xpath', '//*[@id="guid-3768879500"]/div/div[1]/div/div/span')
        try:
            self.assertIn("全部房源", ret)
            mylogger.info('断言成功')
            time.sleep(2)
            self.driver.base_get_image('断言成功截图')
        except Exception as e :
            mylogger.error('断言失败的原因是{}'.format(e))
            time.sleep(2)
            self.driver.base_get_image('断言失败截图')
        self.driver.base_quit_browser()
        mylogger.info('浏览器关闭并推出服务')

    def tearDown(self):
        print("每个用例之后执行一次")
        self.driver.base_quit_browser()  # 后置退出浏览器

    # def main(self):
    #     stat =time.time()
    #     p1 = Process(target=self.test_01, args= 'test01')
    #     p1.start()
    #     p2 = Process(target=self.test_02, args= 'test02')
    #     p2.start()
    #     p1.join()
    #     p2.join()
    #     end = time.time()
    #     print('共消耗{}'.format(end-stat))
        
if __name__ == "__main__":
    stat = time.time()
    threads = []  # 定义一个线程池
    # 线程池
    t1 = threading.Thread(target='test_01')
    threads.append(t1)  # 把t2线程装到线程池里
    t2 = threading.Thread(target='test_02')
    threads.append(t2)  # 把t3线程装到线程池里
    for t in threads:
        t.start()
    end = time.time()
    print('共消耗{}'.format(end-stat))





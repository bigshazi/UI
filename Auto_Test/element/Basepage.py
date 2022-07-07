import os
import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from Auto_Test.element.log import GetLogger

log = GetLogger(logger='Basepage').get_logger()

class Basepage():
    """
        定义一个页面基类，让所有页面都继承这个类，封装一些常用的页面操作方法到这个类
    """
    def __init__(self,driver):
            self.driver = driver
            log.info('[base]:正在获取driver对象：{}'.format(driver) )
    #查找元素方法 封装
    def find_element(self, type, element):
        """根据类型查找元素"""
        dr = ''
        if type == 'id':
            dr = self.driver.find_element(By.ID,element)
        if type == 'name':
            dr = self.driver.find_element(By.NAME,element)
        if type == 'xpath':
            dr = self.driver.find_element(By.XPATH,element)
        if type == 'link_text':
            dr = self.driver.find_element(By.LINK_TEXT,element)
        if type == 'text':
            dr = self.driver.find_element(By.PARTIAL_LINK_TEXT,element)
        if type == 'tag_name':
            dr = self.driver.find_element(By.TAG_NAME,element)
        if type == 'class_name':
            dr = self.driver.find_element(By.CLASS_NAME,element)
        return  dr

    # def base_find(self, loc, timeout=20, poll=0.5):
    #     log.info("[base]: 正在定位:{} 元素".format(loc))
    #     # 使用显示等待查找元素
    #     return WebDriverWait(self.driver,
    #                          timeout=timeout,
    #                          poll_frequency=poll).until(lambda x: x.find_element(*loc))

    #     # 实现H5页面展示
    def showH5(self):
        mobile_emulation = {'deviceName': 'iPhone X'}
        options = webdriver.ChromeOptions()
        options.add_experimental_option('mobileEmulation', mobile_emulation)
        self.driver = webdriver.Chrome(r'D:\Win_TestEngineLite_20210120\chromedriver.exe', chrome_options=options)
        self.driver.set_window_size(375,812)
        self.driver.maximize_window()
        self.driver.implicitly_wait(8)


    # #浏览器后退
    def base_back(self):
        log.info("浏览器后退")
        self.driver.back()

    # #浏览器前进
    def base_forward(self):
        log.info("浏览器前进")
        self.driver.forward()

    # #打开浏览器
    def base_open_url(self,url):
        log.info("正在打开{}页面".format(url))
        self.driver.get(url)

    # #关闭并停止浏览器服务
    def base_quit_browser(self):
        log.info("关闭并停止浏览器")
        self.driver.quit()

    # #刷新浏览器
    def base_refresh_browser(self):
        log.info("正在刷新浏览器")
        self.driver.refresh()

    #等待
    def base_wait(self,time):
        log.info("浏览器等待{}秒".format(time))
        self.driver.implicitly_wait(time)

    #点击元素方法
    def base_click(self,type,element):
        el = self.find_element(type,element)
        try:
            el.click()
            log.info("[base]:正在对:{} 元素实行点击事件".format(element))
        except NameError as e :
            log.error("无法单击元素 %s" % e)

    #输入元素方法
    def base_input(self,type,element,value):
        log.info("[base]:正在对：{}元素输入{}".format(element,value))
        #获取元素
        el = self.find_element(type,element)
        #清空 这里应该是为了清空自带的值
        el.clear()
        #输入
        el.send_keys(value)

    #获取文本信息
    def base_get_text(self,type,element):
        log.info("[base]:正在获取：{}元素文本值".format(element))
        dr = self.find_element(type,element).text
        return dr #返回获取的文本值

    #截图方法
    def base_get_image(self,name):
        #截图并保存在img文件夹下
        file_path = os.path.dirname(os.getcwd()) + '/screenshots/' #查找根目录下的文件夹地址
        rq = time.strftime('%Y年%m月%d日%H时%M分%S秒', time.localtime(time.time()))
        screen_name = file_path + name + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            log.info("[base]: 开始截图并保存")
        except Exception as e:
            log.error("出现异常",format(e))

    #判断元素是否存在于页面
    def base_element_is_exist(self,type,element):
        try:
            self.find_element(type,element)
            log.info("[base]:{}元素查到成功，存在于当前页面".format(element)) #这里的format方法把元素值放到了{}钟
            return True #代表元素存在
        except:
            log.info("[base]:{}元素查找s失败，不存在当前页面".format(element))
            return False #代表元素不存在

    #切换到新页面
    def base_handle(self):
        sleep(1)
        log.info("[base]:切换到新页面")
        h = self.driver.current_window_handle
        hs = self.driver.window_handle
        for newh in hs:
            if newh != h:
                self.driver.switch_to.window(newh) #switch_to 切换页面方法

    # 获取所有句柄并调换到第一个句柄页
    def base_get_handle(self):
        self.driver.switch_to.window(self.driver.window_handle[0])

    #获取alert错误提示
    def base_get_alert(self):
        alert = self.driver.switch_to.alert.text
        return alert

    #跳过alert提示
    def base_jump_alert(self):
        self.driver.switch_to.alert.dismiss()

    #鼠标悬停
    def base_mouse_over(self,type,element):
        log.info("[base]:鼠标悬停{}元素".format(element))
        el = self.find_element(type,element)
        ActionChains(self.driver).move_to_element(el).perform()#参考文档https://www.cnblogs.com/colin2012/p/8872291.html

    #鼠标移动元素-坐标
    def base_mouse_mover(self,type,element,x,y):
        log.info("[base]:鼠标移动{}元素".format(element))
        el = self.find_element(type,element)
        ActionChains(self.driver).drag_and_drop_by_offset(el,x,y).perform()

    #鼠标点击坐标
    def base_mouse_touch_tap(self,x,y,duration=100):
        log.info("[base]:鼠标点击{}x位置和{}y位置".format(x,y))
        screen_width = self.driver.get_window_size()['width']  # 获取当前屏幕的宽
        screen_height = self.driver.get_window_size()['height']  # 获取当前屏幕的高
        a = (float(x) / screen_width) * screen_width
        x1 = int(a)
        b = (float(y) / screen_height) * screen_height
        y1 = int(b)
        self.driver.tap([(x1, y1), (x1, y1)], duration)

    #切换frame表单方法
    def base_switch_frame(self,type,element):
        log.info("[base]:切换到{}fram表单".format(element))
        el = self.find_element(type,element) #获取表单元素
        self.driver.switch_to.frame(el)

    # 回到默认目录方法
    def base_default_content(self):
        log.info("[base]:回到默认目录")
        self.driver.switch_to.default_content()

    # 键盘操作
    def key_enter(self, element):
        """
        回车
        """
        self.find_element(element).send_keys(Keys.ENTER)
        log.info("对%s进行回车" % element['element_name'])

    def key_ctrl_a(self,type,element):
        """
        全选
        """
        self.find_element(type,element).send_keys(Keys.CONTROL, 'a')
        log.info("对%s全选" % element['element_name'])

    def key_ctrl_c(self,type,element):
        """
        复制
        """
        self.find_element(type,element).send_keys(Keys.CONTROL, 'c')
        log.info("对%s复制" % element['element_name'])

    def key_ctrl_v(self,type,element):
        """
        粘贴
        """
        self.find_element(type,element).send_keys(Keys.CONTROL, 'v')
        log.info("对%s粘贴" % element['element_name'])

    def key_ctrl_x(self,type,element):
        """
        剪切
        """
        self.find_element(type,element).send_keys(Keys.CONTROL, 'x')
        log.info("对%s剪切" % element['element_name'])




    











import logging
import time

import pytest
from _pytest.fixtures import fixture

from Auto_Test.element.Basepage import Basepage



def test_01():
    global name
    driver = Basepage('driver')
    # 切换成H5显示
    driver.showH5()
    #打开拍卖首页
    driver.base_open_url('https://market.m.taobao.com/app/pm/new-main/home?pha=true&disableNav=YES')
    #点击我的
    driver.base_click('id','tab-3')
    time.sleep(2)
    #获取当前页面的url
    url = driver.get_url()
    print(url)
    #断言
    assert  'https://market.m.taobao.com/app/pm/rax-tesla/pages/my?disableNav=YES' in url
    #切换iframe框架并进入表单
    driver.base_switch_frame('xpath', '/html/body/div[3]/iframe')
    #点击切换成账号密码登录
    tr = driver.base_element_is_exist('xpath',"//div[@class='login-blocks login-links']")

    if tr is True :
        driver.base_click('xpath', '/html/body/div/div/div[2]/div/form/div[4]/a')
        logging.info('切换成账号密码登录')
    time.sleep(2)
    #获取账号和密码
    start = time.time()
    print(start)
    data = driver.query("select * from student")
    end = time.time()
    print("用时"+ str(end-start))
    name = ''
    password = ''
    for id,name,password in data :
        print(id,name,password)

    #测试sql查询速度
    start2= time.time()
    data2 = driver.query("select name,password from student")
    end2 = time.time()
    print("用时2"+ str(end2-start2))
    for name,password in data2 :
        print(name,password)

    #输入账号名
    driver.base_input('id','fm-login-id',name)
    time.sleep(2)
    #输入密码
    driver.base_input('id','fm-login-password',password)
    time.sleep(2)
    #点击勾选复选框
    driver.base_click('xpath','//*[@id="login-form"]/div[6]/div/label')
    time.sleep(2)
    #点击登录
    driver.base_click('class',"fm-button fm-submit password-login")
    time.sleep(2)



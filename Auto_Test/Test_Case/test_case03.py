import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import traceback

##所见即所得验证


def test_01():
    #切换成H5显示
    global divs, result
    mobile_emulation = {'deviceName': 'iPhone X'}
    options = webdriver.ChromeOptions()
    options.add_experimental_option('mobileEmulation', mobile_emulation)
    wb = webdriver.Chrome(r'D:\Win_TestEngineLite_20210120\chromedriver.exe', chrome_options=options)
    wb.set_window_size(375, 812)
    wb.maximize_window()
    wb.implicitly_wait(5)

    #打开文件取出url每次取一个链接
    file = "D:\yunzhuti.xlsx"
    df =pd.read_excel(file,sheet_name='Sheet1')
    print("******")
    for urls in df.values:
        url = str(urls).replace("['","").replace("']","")+ '&itemId=684157130754'
        # 打开页面
        wb.get(url)
        # #获取页面div，并判断组件名
        try:
            divs = wb.find_elements(By.XPATH, "//div[@class='rax-view rax-scrollview-webcontainer']/div")
        except Exception as e:
            print(format(e))
        if divs == []:
            divs = wb.find_elements(By.XPATH, '//*[@id="scoll_view"]/div')
        xpath = ""
        for div in divs:
            data_spm = div.get_attribute('data-spm')
            data_spm = str(data_spm)
            if "puimod-zhuti-combo-list" in data_spm:
                # 获取下标，下标+1是位置
                data_spm_index = data_spm.index("_") + 1
                # 从位置截取到结束
                uuid = data_spm[data_spm_index:]
                # 这里获取div的数量，判断是否为1*1样式
                divs_xpath = '//*[@id="guid-list-' + uuid + '-0"]/div/div'
                divs2 = len(wb.find_elements(By.XPATH, divs_xpath))
                xpath2 =''
                if divs2 == 1:  # 等于1时是1*1样式
                    xpath2 = '-0"]/div/div/a'
                if divs2 == 2:  # 等于2时是1*2样式
                    xpath2 = '-0"]/div/div[1]/a'
                # 拼接出第一个坑位的xpath
                xpath = '//*[@id="guid-list-' + uuid + xpath2
            elif "puimod-search-list" in data_spm:
                # 获取下标，下标+1是位置
                data_spm_index = data_spm.index("_") + 1
                # 从位置截取到结束
                uuid = data_spm[data_spm_index:]
                # 拼接出第一个坑位的xpath
                xpath = '//*[@id="guid-list-' + uuid + '-0"]/div[1]/a'
            elif "puimod-item-all-module" in data_spm:
                # 获取下标，下标+1是位置
                data_spm_index = data_spm.index("_") + 1
                # 从位置截取到结束
                uuid = data_spm[data_spm_index:]
                # 拼接出第一个坑位的xpath
                xpath = '//*[@id="guid-list-' + uuid + '-0"]/div/div[1]/div[1]/a'
            elif "puimod-rax-list-item-module" in data_spm:
                # 获取下标，下标+1是位置
                data_spm_index = data_spm.index("_") + 1
                # 从位置截取到结束
                uuid = data_spm[data_spm_index:]
                # 拼接出第一个坑位的xpath
                xpath = '//*[@id="guid-list-' + uuid + '-0"]/div/div/div[1]/a'
            # print(data_spm)
        # 点击第一个坑位
        wb.find_element(By.XPATH, xpath).click()
        time.sleep(1)
        # 获取跳转的页面链接
        url2 = wb.current_url
        # 断言，判断链接中是否带itemId=684157130754
        itemId = '684157130754'
        if itemId in url2 :
            pass
        else:
            print("无所见即所得页面："+url)
        print("***********")
    wb.close()


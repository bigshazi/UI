import io
import os
from tkinter import Image

import pytest
import requests

from Auto_Test.common.common_util import common_util
from Auto_Test.common.requests_util import RequestUtil
from Auto_Test.common.yaml_util import read_yaml, get_object_path


class Test_um(common_util):
    # @pytest.mark.parametrize("arg1,arg2",[["name","百里"],["age","12"]])
    # def test_06(self,arg1,arg2):
    #     print("测试06"+str(arg1)+"" +str(arg2))

    code_url=''
    @pytest.mark.parametrize("caseinfo",read_yaml('Test_Case/user_manage/get_project_list_info.yaml'))
    def test_get_project_list_info(self,caseinfo):
    #接口文档地址https://wanandroid.com/blog/show/2
        name    = caseinfo['name']
        method = caseinfo['request']['method']
        url    = caseinfo['request']['url']
        data   = caseinfo['request']['data']
        validate = caseinfo['validate']
        res = RequestUtil.session.request(method=method,url=url,params=data)
        result = res.json()
        print(result)
    # def test_08(self,um):#使用时直接调函数名
    #     print("测试参数化" + um)
    #     print("测试08")

    # @pytest.mark.parametrize("caseinfo",read_yaml('Test_Case/user_manage/post_file_list.yaml'))
    # def test_post_file_list(self,caseinfo):
    #     # 接口文档地址https://wanandroid.com/blog/show/2
    #     name = caseinfo['name']
    #     method = caseinfo['request']['method']
    #     url = caseinfo['request']['url']
    #     data = caseinfo['request']['data']
    #     validate = caseinfo['validate']
    #     res = RequestUtil.session.request(method=method, url=url, json=data)
    #     result = res.json()
    #     print(result)

    @pytest.mark.parametrize("caseinfo",read_yaml('Test_Case/user_manage/generate_QR_code.yaml'))
    def test_QR_code(self,caseinfo):
        # 接口文档地址https://docs.tenapi.cn/qrcode.html#%E8%AF%B7%E6%B1%82url
        name = caseinfo['name']
        method = caseinfo['request']['method']
        url = caseinfo['request']['url']
        data = caseinfo['request']['data']
        validate = caseinfo['validate']
        res = RequestUtil.session.request(method=method,url=url,params=data)
        print(type(res))
        Test_um.code_url = res.content
        print(Test_um.code_url)
        path = get_object_path() +'screenshots/pics.jpg'
        print(path)
        #将得到的二进制二维码数据生成图片并保存
        with open(path,mode='w+b')as f:
            f.write(Test_um.code_url)
        # # byte_stream = io.BytesIO(Test_um.code_url)  # 请求数据转化字节流
        # # roiImg = Image.open(byte_stream)  # Image打开二进制流Byte字节流数据
        # imgByteArr = io.BytesIO()  # 创建一个空的Bytes对象
        # Test_um.code_url.save(imgByteArr, format='PNG')  # PNG就是图片格式
        # imgByteArr = imgByteArr.getvalue()  # 保存的二进制流
        # path = get_object_path() +'screenshots'
        # name = 'test.png'
        # # 生成文件目录
        # if not os.path.exists(path):
        #     os.makedirs(path)
        # # 创建图片
        # with open(path + name, "wb+") as f:
        #     f.write(imgByteArr)

    @pytest.mark.parametrize("caseinfo", read_yaml('Test_Case/user_manage/parse_QR_code.yaml'))
    def test_parse_QR_code(self,caseinfo):
        # 接口文档地址https://docs.tenapi.cn/qrcode.html#%E8%AF%B7%E6%B1%82url
        name = caseinfo['name']
        method = caseinfo['request']['method']
        url = caseinfo['request']['url']
        data = caseinfo['request']['data']
        validate = caseinfo['validate']
        res = RequestUtil.session.request(method=method,url=url,params=data)
        result = res.json()
        print(result)





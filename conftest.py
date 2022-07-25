import pytest




# @pytest.fixture(scope="session",autouse=True,name='all') #使用fixture不用再去继承基础类
# def all():
#     print("执行sql")
#     yield  "db" #返回参数
#     print("关闭数据库链接")
#
# @pytest.fixture(scope="class",autouse=True,name='login') #使用fixture不用再去继承基础类
# def login():
#     print("登录前")
#     yield  "login" #返回参数
#     print("登录之后")
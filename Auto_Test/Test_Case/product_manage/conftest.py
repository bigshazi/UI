import pytest


@pytest.fixture(scope="function",name='pm') #使用fixture不用再去继承基础类
def product_manage():
    print("fixture")
    yield  'pm' #返回参数
    print("fixture之后")
import pytest

from Auto_Test.common.common_util import common_util


class Test_pm(common_util):

    def test_01(self):
        assert 'a' in 'efc'
        print("测试01")

    def test_02(self):
        assert 1==1
        print("测试02")


    def test_03(self,pm):#使用时直接调函数名
        print("测试参数化" + pm)
        print("测试03")
        #print(exe_database_sql)




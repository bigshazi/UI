
import os
import unittest
from BeautifulReport import BeautifulReport
#单元测试
#测试用例路径
test_case_path =  r'D:\test\UI\Auto_Test\Test_Case'
#测试报告存储路径
report_dir = os.path.dirname(os.getcwd()) + '/Test_Result/Test_Report/'
#设置报告的名称
filename = "UI自动化测试报告"
#用例名称
description = "测试搜索框"
#需要执行那些用例，如果目录下的全部，改成"*.py",如果是部分带test后缀的，可以改成“*test.py”
pattern = 'test_case01.py'

if __name__ == '__main__':
       #利用discover（）方法去加载一个路径下所有的测试用例
       test_suite =  unittest.defaultTestLoader.discover(test_case_path,pattern=pattern)
       result = BeautifulReport(test_suite)
       result.report(filename=filename,description=description,report_dir=report_dir)
       runner = unittest.TextTestRunner()
       runner.run(test_suite)

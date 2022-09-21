import os
import time

import pytest

if __name__ == '__main__':
    pytest.main()#执行所有用例
    time.sleep(3)
    print('cssss')
    # os.system("allure generate ./temps -o ./Test_Result/Test_Report --clean")
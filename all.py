import os

import pytest

if __name__ == '__main__':
    pytest.main()
    # 生成allure报告
    os.system("allure generate ../TestReport/temp -o ../TestReport/report --clean")
    # 打开allure报告
    os.system("allure open -h 127.0.0.1 ../TestReport/report")
    # pytest.main(['-vs','./model2_testcase'])
    # pytest.main(['-vs', './model2_testcase/test_func1.py::TestFunc1::test_02'])
    # pytest.main(['-vs --reruns=2','./model2_testcase'])
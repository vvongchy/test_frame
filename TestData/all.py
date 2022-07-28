import os

import pytest

if __name__ == '__main__':
    pytest.main()
    os.system("allure generate ./temp -o ./report --clean")
    # pytest.main(['-vs','./model2_testcase'])
    # pytest.main(['-vs', './model2_testcase/test_func1.py::TestFunc1::test_02'])
    # pytest.main(['-vs --reruns=2','./model2_testcase'])
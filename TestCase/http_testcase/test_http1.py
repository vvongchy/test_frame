import allure
import pytest

from Common.Excel_op import ExcelUnit
from Core.Http_type_case import http_run_case
from Setting.config import Script_path


# 先做数据格式化 再传
# @allure.epic("http类型的测试demo")
@allure.feature("http类型的测试demo")
class TestHttp:
    test_data_path = r"E:\test_work\test_frame\TestData\测试数据"
    test_case_file_path = r"E:\test_work\test_frame\TestData\test_case.xlsx"

    # b = yamlUnit(r"E:\test_work\test_frame\TestData\test_case.yaml").read_yaml()
    # print(a)
    # print(b)

    # @pytest.mark.run(order=1)
    # @pytest.mark.parametrize("a,b",[("1","2"),(1,2)])
    # @pytest.mark.skip( reason= "test case")
    # @pytest.mark.skipif(age>=18,reason="age>18")
    @allure.story("测试用例demo")
    @pytest.mark.parametrize("args", ExcelUnit().format_data(test_case_file_path, Script_path, test_data_path))
    def test(self, args,factory):
        http_run_case(args,factory)

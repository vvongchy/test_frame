import json
import allure
import pytest
from Common.Excel_op import ExcelUnit
from Core.Http_type_case import http_run_case
from Setting.config import Script_path


@allure.feature("http类型的测试demo")
class TestHttp:
    test_data_path = r"E:\test_work\test_frame\TestFile\测试数据"
    test_case_file_path = r"E:\test_work\test_frame\TestFile\test_case.xlsx"

    @allure.story("测试用例demo")
    @pytest.mark.parametrize("args", ExcelUnit().format_data(test_case_file_path, Script_path, test_data_path))
    def test(self, args, factory):
        http_run_case(args, factory)

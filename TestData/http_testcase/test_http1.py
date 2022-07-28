import json

import allure
import pytest

import Common.request_op

from Common.request_op import RequestUnit
from Common.Excel_op import ExcelUnit
from Common.yeml_op import yamlUnit
from Setting.config import Script_path


# 先做数据格式化 再传
@allure.feature("测试用demo类")
class TestHttp:
    test_data_path = r"E:\test_work\test_frame\TestFile\测试数据"
    test_case_file_path = r"E:\test_work\test_frame\TestFile\test_case.xlsx"

    # b = yamlUnit(r"E:\test_work\test_frame\TestFile\test_case.yaml").read_yaml()
    # print(a)
    # print(b)

    # @pytest.mark.run(order=1)
    # @pytest.mark.parametrize("a,b",[("1","2"),(1,2)])
    @allure.story("测试用例demo")
    @pytest.mark.parametrize("args", ExcelUnit().format_data(test_case_file_path, Script_path, test_data_path))
    def test(self, args):
        allure.dynamic.title("用例："+str(args["序号"]))
        allure.dynamic.description(args["步骤描述"])

        # 其他属性
        # allure.dynamic.feature('动态feature')
        # allure.dynamic.story('动态story')
        # allure.dynamic.link("https://www.cnblogs.com/longronglang/category/1859053.html", '动态Link')
        # allure.dynamic.issue("https://www.cnblogs.com/longronglang/category/1859053.html", '动态Issue')
        # allure.dynamic.testcase("https://www.cnblogs.com/longronglang/category/1859053.html", '动态testcase')


        with allure.step("数据预处理"):
            request_method = args["测试脚本"]["method"]
            url = args["测试脚本"]["url"]
            data_type = args["测试脚本"]["data_type"]
            return_data_type = args["测试脚本"]["return_data_type"]
            front = args["前置条件"]
            datas = args["输入数据"]
            expection = args["期望"]
            allure.attach(body=str(front), name="前置条件", attachment_type=allure.attachment_type.TEXT)
            allure.attach(body=str(datas), name="输入数据", attachment_type=allure.attachment_type.TEXT)
            allure.attach(body=str(expection), name="期望", attachment_type=allure.attachment_type.TEXT)
        with allure.step("数据处理"):
            for key, value in datas.items():
                if value in front.keys():
                    datas[key] = front[value]
            allure.attach(body=str(datas), name="处理后数据", attachment_type=allure.attachment_type.TEXT)
            # allure.attach(body=""), name="处理后数据", attachment_type=allure.attachment_type.json)

            # allure.attach(body, name, attachment_type, extension)

        with allure.step("发送请求"):
            res = RequestUnit().send_request(request_method, url, datas, data_type)

        with allure.step("校验期望"):
            if return_data_type == "json":
                res = res.json()
            else:
                res = res.text
            RequestUnit().expectation_assert(expection,res)

import allure

from Core.Request_op import RequestUnit
from Log.LogEntity import logger
from conftest import test_create_file_session, read_temp_file, get_newest_file


def http_run_case(args, factory):
    allure.dynamic.title("用例：" + str(args["序号"]))
    allure.dynamic.description(args["步骤描述"])
    case_name = args["案例名称"]
    logger.info(f"执行案例：{case_name} -----------------------")
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
        headers = args["测试脚本"]["headers"]
        cookies = args["测试脚本"]["cookies"]

        front = args["前置条件"]
        datas = args["输入数据"]
        expection = args["期望"]
        allure.attach(body=str(front), name="前置条件", attachment_type=allure.attachment_type.TEXT)
        allure.attach(body=str(datas), name="输入数据", attachment_type=allure.attachment_type.TEXT)
        allure.attach(body=str(expection), name="期望", attachment_type=allure.attachment_type.TEXT)

    with allure.step("数据处理"):
        # for key, value in datas.items():
        #     if value in front.keys():
        #         datas[key] = front[value]
        format_data = {key: front[value] for key, value in datas.items() if value in front.keys()}
        format_data = {**datas, **format_data}
        allure.attach(body=str(format_data), name="处理后数据", attachment_type=allure.attachment_type.TEXT)
        logger.info(f"input_data:{format_data}")
        # allure.attach(body=""), name="处理后数据", attachment_type=allure.attachment_type.json)
        # allure.attach(body, name, attachment_type, extension)

    with allure.step("临时变量"):
        temp_data = read_temp_file(get_newest_file(r"../tempfile"))
        # 将前置条件合并
        temp_data = {**front, **temp_data}
        allure.attach(body=str(temp_data), name="data", attachment_type=allure.attachment_type.TEXT)
    with allure.step("发送请求"):
        allure.attach(body=str(args["测试脚本"]), name="脚本信息", attachment_type=allure.attachment_type.TEXT)
        res = RequestUnit().send_request(request_method, url, datas, data_type, headers, cookies)

    with allure.step("校验期望"):
        if return_data_type == "json":
            res = res.json()
        else:
            res = res.text
        allure.attach(body=str(res), name="返回数据", attachment_type=allure.attachment_type.TEXT)
        # 断言
        RequestUnit().expectation_assert(expection, res)
        logger.info(f"返回数据：{res}")

    with allure.step("执行结果转化"):
        if isinstance(res, dict):
            processed_res = {("varc_" + str(key)): value for key, value in res.items()}
        temp_var = {**front, **processed_res}
        test_create_file_session(factory, temp_var)
        allure.attach(body=str(temp_var), name="处理后数据", attachment_type=allure.attachment_type.TEXT)

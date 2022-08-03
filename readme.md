# pytestDemo

本项目实现接口自动化的Demo：**Python+Pytest+Requests+Pandas+Allure** 

通过 Python+Requests 来发送和处理HTTP协议的请求接口，使用 Allure 来生成测试报告

使用 Pytest 作为测试执行器，使用 Pandas 处理数据 ，仅需按照模板写Excel就能使用该测试框架demo

## 项目说明

测试数据通过Excel保存，将测试用例拆分出输入数据、前置条件、脚本以便于测试用例的编写。

在读取一个用例文件（test_case）时，通过pandas处理所有涉及到的Excel数据，格式化后传入测试用例类，通过pytest进行测试用例的执行。

在用例执行后，得到的返回数据会打上varc_前缀，作为临时变量保存(tmp_path_factory），下一个用例执行时可以进行调用。

## 框架使用

测试数据包括**测试用例**（test_case）、**输入数据**(test_data)、**前置**(test_front)、**脚本文件**(script)

前置条件格式：文件名|序号   test_front.xlsx|1

输入数据格式：文件名|序号   test_data.xlsx|1

输入数据保存的是测试用例中用到的入参数据

前置保存的是测试用例中需要执行的前置条件（sql或者变量赋值）

脚本配置脚本参数，比如http接口的相关信息（url headers method 等）

前置条件和输入数据需要在测试用例同目录下的测试数据文件夹中（可修改）

## 项目结构

- Log ====>> 日志模块
- Common ====>> 常用公共操作，如Excel文件数据处理、Yaml文件数据处理
- Core ====>> requests方法封装、测试用例处理方法封装
- Setting ====>> 设置，管理配置参数
- TestCase ====>> 测试用例
- TestData ====>> 测试用例的数据
- TempFile ====>> 执行测试时生成的临时文件
- TestReport ====>> 测试报告
- pytest.ini ====>> pytest配置文件
- requirements.txt ====>> 相关依赖包文件
- testcases ====>> 测试用例
- all.py ====>> 执行入口
- conftest.py ====>> 前置


## 测试报告效果展示



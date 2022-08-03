import ast
import json
import os

import pytest




#
# @pytest.fixture(scope="function", autouse=False, params=["p1", "p2"])
# def my_fix(request):
#     print("执行前置" + request.param)
from Log.LogEntity import logger


@pytest.fixture
def factory(tmpdir_factory):
    """
    临时文件
    :param tmpdir_factory:
    :return:
    """
    return tmpdir_factory.mktemp("temp")


def test_create_file_case(tmpdir, datas):
    p = tmpdir.join("temp_data.txt")
    p.write(str(datas))


def test_create_file_session(tmpdir_factory, datas):
    p = tmpdir_factory.join("temp_data.txt")
    p.write(str(datas))


def read_temp_file(file):
    data = {}
    if ".txt" in file:
        try:
            with open(file, "r", encoding='gbk') as f:  # 打开文本
                data = f.read()  # 读取文本
                data = ast.literal_eval(data)
        except Exception as e:
            pass
    else:
        logger.debug("read_temp_file:无临时文件读取")

    return data


def get_newest_file(path):
    # 获取文件夹中所有的文件(名)，以列表形式返货
    L1 = []
    for root, dirs, files in os.walk(path):
        for file in files:
            L1.append(os.path.join(root, file))

    L1.sort(key=lambda x: os.path.getmtime((path + "\\" + x)) if not os.path.isdir((path + "\\" + x)) else 0)
    # print(L1)
    # 获取最新文件的绝对路径，列表中最后一个值,文件夹+文件名
    if L1:
        file_new = os.path.join(convert_path(L1[-1]))
    else:
        file_new = ""
    # print("时间排序后的的文件夹列表：\n %s \n" % lists)

    # print("最新文件路径:\n%s" % file_new)
    return file_new


def convert_path(path: str) -> str:
    """
    转化path
    :param path:
    :return:
    """
    seps = r'\/'
    sep_other = seps.replace(os.sep, '')
    return path.replace(sep_other, os.sep) if sep_other in path else path


# if __name__ == '__main__':
#     # get_newest_file(r"../tempfile")
#     read_temp_file(r"..\tempfile\temp3\temp_data.txt")

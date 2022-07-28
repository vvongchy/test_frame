import os
import re
from pprint import pprint

import numpy as np
import pandas as pd
import openpyxl

from Log.LogEntity import LogUtil

logger = LogUtil("test_project").getLogger()


class ExcelUnit:
    def __init__(self, name=None):
        self.name = name

    # 打开 Excel
    def open_excel(self, file, is_header=0):
        """
        打开Excel返回dataframe
        :param file: Excel文件地址
        :param is_header: None:有行头 / 0：无行头
        :return: dataframe
        """
        try:
            dataframe = pd.read_excel(file, dtype="str", keep_default_na=False, header=is_header)
        except:
            logger.error(f"打开文件 - {file} - 失败", exc_info=True)
        return dataframe

    def read_front(self, file, is_header=0):
        dic = {}
        dataframe = self.open_excel(file, is_header=0)
        front_array = dataframe.loc[:, ["前置条件"]].values
        number_array = dataframe.loc[:, ["序号"]].values
        it = np.nditer([number_array, front_array], flags=['refs_ok', 'c_index'],
                       op_flags=['readwrite'])
        for number, front in it:
            temp_dict = {}
            for i in str(front).split(";"):
                if "=" in i:
                    temp_list=str(i).split("=")
                    temp_dict[temp_list[0]] = temp_list[1]
            dic[str(number)] = temp_dict
        return dic

    def read_data(self, file, is_header=0):
        df_dict = {}
        dataframe = self.open_excel(file, is_header=0)
        number_array = dataframe.loc[:, ["序号"]].values
        # a = dataframe.iloc[:,2].values
        row_head_list = dataframe.axes[1].tolist()
        for number_array, i in zip(number_array, dataframe.index.values):
            # loc为按列名索引 iloc 为按位置索引，使用的是 [[行号], [列名]]
            df_line = dataframe.loc[i, row_head_list].to_dict()
            df_dict[str(number_array[0])] = df_line
        # pprint(df_dict)
        return df_dict

    def read_script(self, file):
        """
        :param path: 文件位置
        :return:
        """
        # 创建最终返回的空字典
        df_dict = {}
        # 读取Excel文件
        df = self.open_excel(file)

        # 替换Excel表格内的空单元格，否则在下一步处理中将会报错
        df.fillna("", inplace=True)

        script_name_array = df.loc[:, ["脚本名"]].values
        for script_name, i in zip(script_name_array, df.index.values):
            # loc为按列名索引 iloc 为按位置索引，使用的是 [[行号], [列名]]
            df_line = df.loc[i, ['脚本类型', 'method', 'url', 'data_type', 'return_data_type', 'header', '备注']].to_dict()
            # 将每一行转换成字典后添加到列表
            df_dict[str(script_name[0])] = df_line
        # pprint(df_dict)
        return df_dict

    def read_case(self, file):
        df_list = []
        dataframe = self.open_excel(file, is_header=0)
        # number_array = dataframe.loc[:, ["序号"]].values
        # a = dataframe.iloc[:,2].values
        row_head_list = dataframe.axes[1].tolist()
        # for number_array, i in zip(number_array, dataframe.index.values):
        for i in dataframe.index.values:
            # loc为按列名索引 iloc 为按位置索引，使用的是 [[行号], [列名]]
            df_line = dataframe.loc[i, row_head_list].to_dict()
            df_list.append(df_line)
        # pprint(df_dict)
        return df_list

    def read_test_data(self, path):
        xlsx_list = self.get_xlsx_file(path)
        temp_dict = {}
        for file in xlsx_list:
            if "_data" in file:
                temp_dict[os.path.basename(file)] = self.read_data(file)
            elif "_front" in file:
                temp_dict[os.path.basename(file)] = self.read_front(file)
        # print(temp_dict)
        return temp_dict

    def format_data(self, case_file, script_file, path):
        """

        :param file:
        :param path:
        :return:
        """
        test_data_dict = self.read_test_data(path)
        data_list = self.read_case(case_file)
        script_dict = self.read_script(script_file)
        # print(script_dict)
        for v in data_list:
            try:
                input_data = str(v["输入数据"]).split("|")
                front = str(v["前置条件"]).split("|")
                v["输入数据"] = test_data_dict[input_data[0]][input_data[1]]
                v["前置条件"] = test_data_dict[front[0]][front[1]]
                v["测试脚本"] = script_dict[v["测试脚本"]]
            except:
                logger.error("测试用例与测试数据对应错误")
        return data_list
        # print(data_dict)

    def get_xlsx_file(self, file_dir):
        """
        获取目录下所有xls/xlsx文件地址
        :param file_dir:
        :return:
        """
        L1 = []
        for root, dirs, files in os.walk(file_dir):
            for file in files:
                if os.path.splitext(file)[1] == '.xls' or os.path.splitext(file)[1] == '.xlsx':
                    L1.append(os.path.join(root, file))
        return L1


if __name__ == '__main__':
    a = ExcelUnit().read_front(r"E:\test_work\test_frame\TestFile\test_front.xlsx")
    # print(a)
    # ExcelUnit().read_data(r"E:\test_work\test_frame\TestFile\test_data.xlsx")
    # ExcelUnit().read_script(r"E:\test_work\test_frame\TestFile\script.xlsx")
    # ExcelUnit().read_case(r"E:\test_work\test_frame\TestFile\test_case.xlsx")
    # ExcelUnit().read_test_data(r"E:\test_work\test_frame\TestFile\测试数据")

    test_data_path = r"E:\test_work\test_frame\TestFile\测试数据"
    a = ExcelUnit().format_data(r"E:\test_work\test_frame\TestFile\test_case.xlsx",
                                r"E:\test_work\test_frame\TestFile\script.xlsx", test_data_path)
    print(a)

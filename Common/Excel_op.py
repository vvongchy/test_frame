import numpy as np
import pandas as pd
import openpyxl

from Log.LogEntity import LogUtil

logger = LogUtil("test_project").getLogger()


class ExcelUnit:
    def __init__(self, name=None):
        self.name = name

    # 打开 Excel
    def open_excel(self,file, is_header=0):
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


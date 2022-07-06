import pandas as pd

from Common.Excel_op import ExcelUnit
if __name__ == '__main__':
    excelUnit = ExcelUnit()
    dataframe1 = excelUnit.open_excel("test_case.xlsx")
    print(dataframe1)
    # print(dataframe1[1][1])
    # help(pd.read_excel)
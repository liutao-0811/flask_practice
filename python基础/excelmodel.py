# 读取excel的内容

# -*- coding: utf-8 -*-
import xdrlib, sys
import xlrd

row = ""


def open_excel(file=r'F:\flask_practice\python基础\2.xlsx'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception as e:
        print(e, '--->out error message')


# 根据索引获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的所以  ，by_index：表的索引
def excel_table_byindex(file=r'F:\flask_practice\python基础\2.xlsx', colnameindex=0, by_index=0):

    #data = xlrd.open_workbook(file)
    data = open_excel(file)
   # table = data.sheets()[by_index]
    table = data.sheet_by_index(by_index)
    nrows = table.nrows  # 行数
    ncols = table.ncols  # 列数
    colnames = table.row_values(colnameindex)  # 某一行数据 返回的是一个数组吧应该是
    list = []

    '遍历行'
    for rownum in range(0, nrows):
        row = table.row_values(rownum)
        '如果确实有一行，这行不为空'
        if row:
            app = {}
            '遍历列'
            len1 = len(colnames)
            for i in range(0, len1):
                app[colnames[i]] = row[i]
            list.append(app)
    return list


# 根据名称获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的所以  ，by_name：Sheet1名称
# def excel_table_byname(file= 'D:/file.xls',colnameindex=0,by_name=u'Sheet1'):
#     data = open_excel(file)
#     table = data.sheet_by_name(by_name)
#     nrows = table.nrows #行数
#     colnames =  table.row_values(colnameindex) #某一行数据
#     list =[]
#     for rownum in range(0,nrows-1):
#          row = table.row_values(rownum)
#          if row:
#              app = {}
#              for i in range(len(colnames)):
#                 app[colnames[i]] = row[i]
#              list.append(app)
#     return list

def main():
    tables = excel_table_byindex()
    for row in tables:
        print(row)

    #  tables = excel_table_byname()
    # for row in tables:
    #    ' print (row)'


'让你写的脚本模块既可以导入到别的模块中用，另外该模块自己也可执行'
'http://www.jb51.net/article/51892.htm'

if __name__ == "__main__":
    main()

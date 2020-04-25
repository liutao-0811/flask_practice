#coding:utf-8
import xlrd

#读取excel表格的函数
def read_excel():
    #打开文件
    open_files = xlrd.open_workbook(r'C:\Users\13664\Desktop\用例\行业答案&商品答案导入文件\lt123.xlsx')
    #获取工作表
    sheet = open_files.sheet_by_name('Sheet1')
    qs = []
    q_ids = []
    a_ids = []
    #循环读取表格内容
    for i in range(sheet.nrows):
        hang = sheet.row_values(i)  #读取一行数据
        q = hang[0]
        q_id = hang[1]
        a_id = hang[2]
        #将没一列数据依次保存在q ，q_id  ，a_id里面
        qs.append(q)
        q_ids.append(q_id)
        a_ids.append(a_id)
    return qs,q_ids,a_ids
    #print(qs,q_ids,a_ids)
a=read_excel()
print(a)
print(a[0])
print(a[1])
print(a[2])

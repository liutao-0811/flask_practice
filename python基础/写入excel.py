#coding:utf-8
import openpyxl
data = [['小王','22','男'],['小明','223','女']]
def write_excel():
    wf = openpyxl.load_workbook('lt123.xlsx')#读取excel表格
    w_data = wf['Sheet1'] #sheet1工作表
    for i in data:
        w_data.append(i)
    savename = 'lt123.xlsx'
    wf.save(savename)#需要保存的表格
write_excel()

####删除某行 列数据
wb = openpyxl.load_workbook('lt123.xlsx')
ws = wb['Sheet1']
ws.delete_rows(15,1)# 删除从第15行起的1行内容
#ws.delete_cols(1,2)# 删除从第1列起的2列元素
wb.save('家族信息表.xlsx')# 保存表格
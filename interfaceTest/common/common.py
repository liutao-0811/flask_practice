import os
from xlrd import open_workbook
from xml.etree import ElementTree as ElementTree
from interfaceTest.common.Log import Mylog as Log
from interfaceTest.common import configHttp
from interfaceTest.readConfig import proDir

localConfigHttp = configHttp.ConfigHttp()
log =Log.get_log()
logger = log.get_logger()

#从excel中读取测试用例
def get_xlsx(xlsx_name,sheet_name):
    caselist = []
    #get xlsx file‘s path
    xlsxPath = os.path.join(proDir, "testFile", xlsx_name)
    #打开文件
    file = open_workbook(xlsxPath)
    #通过name获取工作表
    sheet = file.sheet_by_name(sheet_name)
    #获取行数
    nrows = sheet.nrows
    for i in range(nrows):
        if sheet.row_values(i)[0] !=u'case_name':#排除第一行
            caselist.append(sheet.row_values(i))

            return caselist

    #从xml文件中读取sql语句
    database = {}
    def set_xml():
        if len(database) == 0:
            sql_path = os.path.join(proDir,"testfile","SQL.xml")
            tree = ElementTree.parse(sql_path)#解析xml并返回解析树
            for db in tree.findall("database"):
                db_name = db.get("name")
                #打印sql_name
                table = {}
                for tb in db.getchildren():
                    table_name = tb.get("name")
                    #打印表名
                    sql = {}
                    for data in tb.getchildren():
                        sql_id = data.get("id")
                        #打印id
                        sql[sql_id] = data.text
                    table[table_name] = sql
                database[db_name] =table

    def get_xml_dict(database_name, table_name):
        set_xml()
        database_dict = database.get(database_name).get(table_name)
        return database_dict

    def get_sql(database_name,table_name,sql_id):
        db = get_xml_dict(database_name,table_name)
        sql = db.get(sql_id)
        return sql

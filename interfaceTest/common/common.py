import os
from xlrd import open_workbook
from xml.etree import ElementTree as ElementTree
from interfaceTest.common.Log import Mylog as Log
from interfaceTest.common import configHttp



localConfigHttp = configHttp.ConfigHttp()
log =Log.get_log()
logger = log.get_logger()

#从excel中读取测试用例
def get_xlsx(xlsx_name,sheet_name):
    caselist = []
    #get xlsx file‘s path
    xlsxPath = os.path.join(proDir, "testFile", xlsx_name)



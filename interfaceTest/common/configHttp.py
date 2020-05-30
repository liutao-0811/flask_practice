import requests
from  interfaceTest import readConfig
from interfaceTest.common.Log import Mylog as Log

localReadConfig = readConfig.ReadConfig()

class ConfigHttp():
    def __init__(self):
        global host, port, timeout
        host = localReadConfig.get_http('baseurl')
        port = localReadConfig.get_http('port')
        timeout = localReadConfig.get_http('timeout')
        self.log = Log.get_log()
        self.logger = self.log.get_logger()
        self.headers = {}
        self.params = {}
        self.data = {}
        self.url = None
        self.files = {}

    def set_url(self,url):
        self.url = host + url

    def set_header(self,header):
        self.headers = header

    def set_params(self,param):
        self.params = param

    def set_data(self,data):
        self.data = data
    def set_files(self,file):
        self.files = file

    #define http  get method
    def get(self):
        try:
            res = requests.get(self.url, params=self.data, headers=self.headers,
                               timeout=float(timeout))
            #返回状态信息
            return res
        except TimeoutError:
            self.logger.error("time out!")
            return None

    #define post method
    def post(self):
        try:
            res = requests.post(self.url, headers=self.headers,data=self.data,files=self.files
                                ,timeout=float(timeout))
            return res
        except TimeoutError:
            self.logger.error("time out!")
            return None
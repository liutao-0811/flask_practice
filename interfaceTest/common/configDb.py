import pymysql
from interfaceTest import readConfig
from interfaceTest.common.Log import Mylog as Log


localReadConfig = readConfig.ReadConfig()
class MyDb():
    global host,username,password,port,database,config
    host =localReadConfig.get_db("host")
    username =localReadConfig.get_db("username")
    password = localReadConfig.get_db("password")
    port = localReadConfig.get_db("port")
    database = localReadConfig.get_db("database")
    config = {
        'host': str(host),
        'username': username,
        'password': password,
        'port': int(port),
        'db': database
    }


    def __init__(self):
        self.log = Log.get_log()
        self.logger = self.log.get_logger()
        self.db = None
        self.cursor = None   #游标对象 cursor

    def connectDB(self):
        try:
            #连接数据库
            self.db = pymysql.connect(**config)
            #创建游标对象
            self.cursor = self.db.cursor()
            print("Connect DB successfully")
        except ConnectionError as er:
            self.logger.error(str(er))

    def excuteSQL(self, sql, params):
        self.connectDB()
        #执行sql   游标执行sql语句
        self.cursor.excute(sql, params)
        #提交数据库执行
        self.db.commit()
        return self.cursor


    def get_all(self, cursor):
        value = cursor.fetchall()
        return value

    """
    使用python的fetchone()、fetchall（）语句提取出来的数据格式是元组数据。
    想要使用这个元组，可以通过如下方法：
        1、游标执行sql语句
        cursor.execute(“select *
        from 表名”)
        2、使用fetchone()
        从数据库中获得元组数据
        data = cursor.fetchone()
        3、这样得到如下数据
        如：（“1”, “章先生”, “18”, “18640811111”）
        则data[0] = 1
        data[1] = 章先生
    """

    def get_one(self,cursor):
        value = cursor.fetchone()
        return value

    def closeDB(self):
        self.cursor.close()  #关闭游标连接
        self.db.close()  #关闭数据库
        print("database  closed!!!")

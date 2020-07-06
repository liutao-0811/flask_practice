import logging,os
from datetime import datetime
import threading
from interfaceTest import readConfig

class Log():
    def __init__(self):
        global logPath, resultPath, proDir
        proDir =readConfig.proDir
        resultPath = os.path.join(proDir,'result')
        #  # create result file if it doesn't exist
        if not os.path.exists(resultPath):
            os.mkdir(resultPath)
        # defined test result file name by localtime
        logPath = os.path.join(resultPath,str(datetime.now().strftime("%Y%m%d%H%M%S")))
        # create test result file if it doesn't exist
        if not os.path.exists(logPath):
            os.mkdir(logPath)
        #define logger
        self.logger = logging.getLogger()  #初始化
        self.logger.setLevel(logging.info())#  defined log level 设置日志级别
        #define handler
        """# Handler对象的作用是（基于日志消息的level）
        # 将消息分发到handler指定的位置（文件、网络、邮件等）。
        # Logger对象可以通过addHandler()方法为自己添加0个或者更多个handler对象。
        """
        handler = logging.FileHandler(os.path.join(logPath,'output.log'))

        """define  Formater对象用于配置日志信息的最终顺序、结构和内容
        """
        formater = logging.Formatter('%(asctime)s - %(name)s - % (levelname)s - %(message)s')
        #定义formater
        handler.setFormatter(formater)
        #add handler
        self.logger.addHandler(handler)

#将日志类放进一个线程内并加锁（保证线程不会乱）：
class Mylog():
    log = None
    mutex = threading.Lock()  #初始化线程并加锁

    def __init__(self):
        pass

    @staticmethod##改静态方法函数里不传入self 或 cls  #静态方法 类或实例均可调用
    def get_log():
        if Mylog.log is None:
            Mylog.mutex.acquire()#获取锁
            Mylog.log = Log()
            Mylog.mutex.release()  #释放锁

        return Mylog.log

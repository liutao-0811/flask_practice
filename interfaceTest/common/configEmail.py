import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
import threading
from interfaceTest import readConfig
from interfaceTest.common.Log import Mylog
import zipfile
import glob

localReadConfig = readConfig.ReadConfig()


class Email():
    def __init__(self):
        global host,user,password, port, sender,title,content
        host = localReadConfig.get_email("mail_host")
        user = localReadConfig.get_email("mail_user")
        password = localReadConfig.get_email("mail_password")
        port = localReadConfig.get_email("mail_port")
        sender = localReadConfig.get_email("mail_sender")
        title = localReadConfig.get_email("mail_title")
        content = localReadConfig.get_email("mail_content")
        self.value =localReadConfig.get_email("recevier")
        self.recevier = []
        #获得接收器列表
        for n in str(self.value).split("/"): #str.split以/分隔 返回个列表
            self.recevier.append(n)
        #定义邮件主题
        date =datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.subject = title + " " + date
        self.log = Mylog.get_log()
        self.logger = self.log.get_logger()
        self.msg = MIMEMultipart('mixed') #定义邮件类型

    """
    MIMEMultipart类型
    MIME邮件中各种不同类型的内容是分段存储的，各个段的排列方式、位置信息都通过Content-Type域的multipart类型来定义。multipart类型主要有三种子类型：mixed、alternative、related。
    （1） MIMEMultipart类型基本格式
    ● MIMEMultipart（‘mixed’）类型
    如果一封邮件中含有附件，那邮件的中必须定义multipart/mixed类型，邮件通过multipart/mixed类型中定义的boundary标识将附件内容同邮件其它内容分成不同的段。基本格式如下：
    msg=MIMEMultipart(‘mixed’)

    ● MIMEMultipart(‘alternative’)类型
    MIME邮件可以传送超文本内容，但出于兼容性的考虑，一般在发送超文本格式内容的同时会同时发送一个纯文本内容的副本，如果邮件中同时存在纯文本和超文本内容，则邮件需要在Content-Type域中定义multipart/alternative类型，邮件通过其boundary中的分段标识将纯文本、超文本和邮件的其它内容分成不同的段。基本格式如下：
    msg=MIMEMultipart(‘alternative’)

    ● MIMEMultipart(‘related’)类型
    MIME邮件中除了可以携带各种附件外，还可以将其它内容以内嵌资源的方式存储在邮件中。比如我们在发送html格式的邮件内容时，可能使用图像作为 html的背景，html文本会被存储在alternative段中，而作为背景的图像则会存储在multipart/related类型定义的段中。基本格式如下：
    msg=MIMEMultipart(‘related’)

    """

    def config_header(self):
        self.msg['subject'] = self.subject
        self.msg['from'] = sender
        self.msg['to'] = ":".join(self.recevier)

    def config_content(self):
        content_path = MIMEText(content, 'plain', 'utf-8')
        self.msg.attach(content_path)

    def config_file(self):
        #if the file content is not null, then config the email file
        if self.check_file():
            reportpath = self.log.get_result_path()
            zippath = os.path.join(readConfig.proDir, "result", "test.zip")
            #zip  file
            files = glob.glob(reportpath + "\*") #获取 reportpath路径下的所有文件
            f = zipfile.ZipFile(zippath, 'w', zipfile.ZIP_DEFLATED)
            """
            ZIP_DEFLATED对应于压缩(或放气)的归档成员(归档中的文件). 
            ZIP_STORED对应于一个存档成员,它只是存储而不是压缩,与tar文件中的存档成员完全相同.
            解压：r
            压缩：w
            追加压缩：a """
            for file in files:
                f.write(file)
            f.close()

            """
            # 添加附件
attachment = MIMEText(_text=open(reportFile, 'rb').read(), _subtype='base64',_charset= 'utf-8')
attachment['Content-Type'] = 'application/octet-stream'
attachment['Content-Disposition'] = 'attachment;filename = "result.html"'
msg.attach(attachment)
            """

            reportfile = open(zippath,'rb').read()
            filehtml = MIMEText(reportfile,'bash64','utf-8')
            filehtml['Content-Type'] = 'application/octet-stream'
            filehtml['Content-Disposition'] = 'attachment; filename="test.zip"'
            self.msg.attach(filehtml)

    def check_file(self):
        reportpath = self.log.get_report_path()
        if os.path.isfile(reportpath) and not os.stat(reportpath) ==0:
            return True
        else:
            return False

    def send_email(self):
        self.config_header()
        self.config_content()
        self.config_file()
        try:
            smtp = smtplib.SMTP()
            self.connect(host)#可加端口号connect(mail_host, 25)
            smtp.login(user, password)
            smtp.sendmail(sender,self.recevier,self.msg.as_string())
            smtp.quit()
            self.logger.info("邮件发送成功.")
        except Exception as ex:
            self.logger.error(ex)

#将发邮件的class放进一个线程内并加锁（保证线程不会乱）：
class MyEmail():
    email =None
    mutex = threading.Lock()

    def __init__(self):
        pass

    @staticmethod
    def get_email():
        if MyEmail.email is None:
            MyEmail.mutex.acquire()#获取锁
            MyEmail.email = Email()
            MyEmail.mutex.release()#释放锁
        return MyEmail.email

if __name__ == '__main__':
    email = MyEmail.get_email()








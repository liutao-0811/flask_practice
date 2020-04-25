import datetime
from datetime import date
import time

##日期时间

a=datetime.datetime(2003,12,1)
b=date.today()
print(a)
print(b)
b1=a+datetime.timedelta(minutes=10)
print(b1)
c=time.time()
c1=time.localtime()
print(c)
print(c1)
print(time.strftime("%H:%M:%S",c1))
c=int(c)
print(c)

import time,random
from threading import Thread,current_thread
from queue import Queue
q=Queue(5)  #声明队列长度
"""
q.put(1)   #put往队列里写入数据
q.put(2)
q.get()    #get提取队列数据
"""



class ProducterThread(Thread):
    def run( self ):
        name = current_thread().getName()
        nums = range(100)
        global q
        while True:
            num = random.choice(nums)
            q.put(num)
            print("生产者 %s 生产了数据 %s" %(name,num))
            t = random.randint(1,3)
            time.sleep(t)
            print("生产者 %s  睡醒了 %s 秒" % (name, t))


class CustomerThread(Thread):
    def run( self ):
        name = current_thread().getName()
        global q
        while True:
            num = q.get()
            q.task_done()
            print("消费者 %s 消费了数据 %s " %(name,num))
            t = random.randint(1,5)
            time.sleep(t)
            print("消费者 %s  睡醒了 %s 秒" % (name, t))


p1= ProducterThread(name='p1')
p1.start()
p2=ProducterThread(name='p2')
p2.start()
c1=CustomerThread(name='c1')
c1.start()



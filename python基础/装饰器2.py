

def decorator_factory(enter_message,exit_message):
    def simple_decorator(f):#f表示调用了hello
        def wrapper():
            print(enter_message)
            f()
            print(exit_message)
        return wrapper
    return simple_decorator

@decorator_factory('start','end')
def hello():
    print('hello word')
hello()

#带参数的被装饰的函数
# 装饰器不带参数showtime ，就将被装饰的函数放在装饰器函数中showtime
import time
def showtime(func):
    def wrapper(a,b):
        start_time = time.time()
        func(a,b)
        end_time = time.time()
    return wrapper

@showtime #add=showtime(add)
def add(a,b):
    print(a+b)
    time.sleep(1)

@showtime #sub=showtime(sub)
def sub(a,b):
    print(a-b)
    time.sleep(1)

add(2,3)
sub(4,3)


#带参数的装饰器(装饰函数),
# 装饰器带了参数 ，就将被装饰的函数放在第一个闭包函数中showtime
def time_logger( flag=0 ):
    def showtime( func ):
        def wrapper( a, b ):
            start_time = time.time()
            func(a, b)
            end_time = time.time()
            print('spend is {}'.format(end_time - start_time))

            if flag:
                print('将此操作保留至日志')

        return wrapper

    return showtime


@time_logger(2)  # 得到闭包函数showtime,add = showtime(add)
def add( a, b ):
    print(a + b)
    time.sleep(1)
add(3, 4)
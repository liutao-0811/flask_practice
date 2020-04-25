import time



"""
#装饰器不带参数
def a( b ):
    print("开始")
    time.sleep(3)
    b()
    print("结束")


@a
def b():
    print("5")


b
"""
#装饰器：带参数
def a( b ):
    def c(x):
        print("开始")
        time.sleep(3)
        b(x)
        print("结束")


    return c

@a
def b(x):
    print(x)


b(2)

print(b.__name__)
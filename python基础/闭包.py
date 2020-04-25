def sum1( a ):
    def add1( c ):
        return a + c

    return add1


num1 = sum1(2)
print(type(num1))
print(num1(4))



def counter():
    cnt=[0]
    def add():
        cnt[0]+=1
        return cnt[0]

    return add
num11=counter()
print("33333")
print(num11)
print("1111")


#a+b+x=y

def fun1(a,b):
   def fun2(x):
        y=a+b+x
        return y


   return fun2

num4=fun1(1,2)
print(type(num4))
num5=num4(3)
print(num5)
print(num4(4))


def f1():
    x = 0
    def counter():
        nonlocal x
        x += 1
        return x

    return counter
b=f1()
print(b())
print(b())
print(b())
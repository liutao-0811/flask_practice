def f1():
    x=0
    def counter():
        nonlocal x
        x+=1
        return x
    return counter

counter=f1()
print(counter())
print(counter())
print(counter())
print(counter())
print(counter())
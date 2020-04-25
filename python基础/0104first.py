list2=range(2,30)
b=iter(list2)
for i in b:
    print(i)

import sys

list1 = range(1, 10)
a = iter(list1)
while True:
    try:
        print(next(a))
    except StopIteration:
        sys.exit()


# def c(x,y,z):
#     while x<y:
#         yield x
#         x+=z
#
# for i in c(2,15,2):
#     print(i)


def c(x,y,z):
    while x<y:
        yield x
        x+=z

for i in c(2,15,2):
    print(i,end=" ")
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 08:01:01 2019

@author: 13664
"""
print(2018%12)
a='asda'
print(a[2])
#计算1-10中偶数的平方
list1=[]
for i in range(1,11):
    if i % 2 == 0:
        i*=i
        print(i)

#方法二：
list2=[i*i for i in range(1,10) if i % 2 == 0]
print(list2)


b=(u'姓名',u'年龄')
#列表推导式、字典推到式
dict1={i:0 for i in b }
print(dict1)

zodiac_name = ((u'摩羯座'),(u'水瓶座'),(u'处女座'),(u'天秤座'),
               (u'白羊座'),(u'双鱼座'),(u'金牛座'),(u'双子座'),
               (u'巨蟹座'),(u'狮子座'),(u'天蝎座'),(u'射手座'))

try:
    with open('2.txt') as file01:
        for line in file01.readlines():
            print(line)
            print("#"*10)
except (NameError, FileNotFoundError, FileExistsError,Exception) as e:
    print("文件不存在%s" %e)
finally:
    file01.close()


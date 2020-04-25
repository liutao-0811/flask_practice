import re
#匹配
p=re.compile('a')
b=p.match('a')
c=p.match('d')
print(b)
print(c)
p1=re.compile('b*a')
d=p1.match('csffbaaaa')
d1=p1.search('csffbaaaa')
print(d)
print(d1)
e=re.match('a{4}','aaabbbccc')
print(e)
f=re.compile(r'(\d+)-(\d+)-(\d+)')
F=f.match('2020-05-04').group(2)
F1=f.match('2020-05-04').groups()
print(F)
print(F1)


print("#"*10)
p3 ='123-1234-5678   #     这是电话号码'
p4=re.sub(r'#.*\S','',p3)
print(p4)
p5=re.sub(r'\D.','',p4)
print(p5)
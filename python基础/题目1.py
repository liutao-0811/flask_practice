#使用python生成包含1000个随机字符的字符串，然后统计每个字符的出现次数。（使用字典）

import random
import string
#string.ascii_letters表示26个大小写字母
#string.digits表示数字
#string.punctuation表示标点符号
x=string.ascii_letters+string.digits+string.punctuation
"""
y=[]
for i in range(1000):
    y=y.append(random.choice(x))
"""
y = [random.choice(x) for i in range(1000)]
#join可将取出的数据连接成字符串
z = "".join(y)
new_dic = dict()
# 重点：循环遍历将取出的字符作为key保存到字典，每个字符出现的次数作为value
# 这里要明白“字典.get(参数1，参数2)”所表达的是什么意思
# ->参数1表示:key值，
# ->参数2:如果指定键的值不存在时，返回该默认值(参数2)
for a in z:
    new_dic[a] = new_dic.get(a, 0) + 1
print(new_dic)
#coding:utf-8
import requests
from bs4 import BeautifulSoup

url = "http://www.mzitu.com"

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}


html = requests.get(url, headers=header)
"""
if html.status_code == 200:
    # 打印结果 .text是打印出文本信息即源码
    print(html.text)
else:
    print("fail")
"""

print("#######################")
#使用自带的html.parser解析，速度慢但通用
soup = BeautifulSoup(html.text,'html.parser')
'''
注意：BeautifulSoup()返回的类型是<class 'bs4.BeautifulSoup'>
find()返回的类型是<class 'bs4.element.Tag'>
find_all()返回的类型是<class 'bs4.element.ResultSet'>
<class 'bs4.element.ResultSet'>不能再进项find/find_all操作

'''


#实际上是第一个class = 'postlist'的div里的所有a 标签是我们要找的信息
all_a = soup.find("div",class_='postlist').find_all('a',target='_blank')

for a in all_a:
    title = a.get_text()#提取文本
    print(title)
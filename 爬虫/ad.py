#coding:utf-8
import requests
from bs4 import BeautifulSoup
import os
all_url = 'http://www.mzitu.com'

#http请求头
header = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
    'Referer': 'http://www.mzitu.com'
}

p_header = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
    'Referer': 'http://i.meizitu.net'
}
#此请求头破解盗链

start_html = requests.get(all_url,headers = header)

#保存地址
path = r'C:\Users\13664\PycharmProjects\lianxi\爬虫\meizi'

#找最大页码
soup = BeautifulSoup(start_html.text,'html.parser')
page = soup.find_all('a',class_ = 'page-numbers')
max_page = page[-2].text


a_url = 'http://www.mzitu.com/page/'
for i in range(1,int(max_page)+1):
    p_url =a_url+str(i)
    start_html =requests.get(p_url,headers = header)
    soup = BeautifulSoup(start_html.text,'html.parser')
    all_a = soup.find('div',class_ = 'postlist').find_all('a',target = '_blank')
    for a in all_a:
        title = a.get_text() #提取文本
        if title != '':
            print("准备爬取："+ title)
        else:
            continue
import requests
from  bs4 import BeautifulSoup

url = 'http://www.mzitu.com/208935'
header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'}

html = requests.get(url,headers = header)
soup = BeautifulSoup(html.text,'html.parser')
#最大页数在span标签中的第10个
pic_max = soup.find_all('span')[9].text
print(pic_max)

"""
#输出每个图片页面地址
for i in range(1,int(pic_max)+1):
    href = url +'/'+str(i)
    print(href)
"""
#找标题
title = soup.find('h2',class_='main-title').text
#输出每个图片页面地址
for i in range(1,int(pic_max)+1):
    herf = url +'/'+str(i)
    html1 = requests.get(herf,headers = header)
    mess = BeautifulSoup(html1.text,'html.parser')
    # 图片具体地址在img标签alt属性和标题一样的地方
    pic_url = mess.find('img',alt = title)
    html2 =requests.get(pic_url['src'],headers =header)
    # 获取图片的名字方便命名
    file_name = pic_url['src'].split(r'/')[-1]
    # 图片不是文本文件，以二进制格式写入，所以是html.content
    f = open(file_name,'wb')
    f.write(html2.content)
    f.close()
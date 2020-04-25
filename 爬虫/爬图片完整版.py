#coding:utf-8
import requests
from bs4 import BeautifulSoup
import os
all_url = 'http://www.mzitu.com'

#http请求头
header = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
    'Connection': 'Keep-Alive',
    'Referer': 'http://www.mzitu.com'
}

p_header = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
    'Connection': 'Keep-Alive',
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
        #win不能创建带？的目录
        if os.path.exists(path+title.strip().replace('?','')):
            flag=1
        else:
            os.makedirs(path+title.strip().replace('?',''))
            flag=0
        os.chdir(path + title.strip().replace('?',''))
        href =a['href']
        html = requests.get(href,headers =header)
        mess = BeautifulSoup(html.text,'html.parser')
        pic_max = mess.find_all('span')
        pic_max = pic_max[9].text #最大页数
        if (flag == 1 and len(os.listdir(path + title.strip().replace('?', ''))) >= int(pic_max)):
            print('已经保存完毕，跳过')
            continue
        for num in range(1,int(pic_max)+1):
            pic = href+'/'+str(num)
            html = requests.get(pic, headers=header)
            mess = BeautifulSoup(html.text, "html.parser")
            pic_url = mess.find('img', alt=title)
            print(pic_url['src'])
            #exit(0)
            html = requests.get(pic_url['src'], headers=p_header)
            file_name = pic_url['src'].split(r'/')[-1]
            f = open(file_name, 'wb')
            f.write(html.content)
            f.close()
        print('完成')
print('第',i,'页完成')
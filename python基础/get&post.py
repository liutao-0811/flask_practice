import requests
url2 = 'http://www.baidu.com'
header ={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'}

response12 = requests.get(url2,params={'wd':'python'},headers=header)
if response12.status_code == 200:
    print(response12.text) #text查看 响应内容

    # 查看完整url地
    print(response12.url)

    # 查看响应头部字符编码
    print(response12.encoding)

    # 查看响应头部字符编码
    print(response12.status_code)
else:
    print('fail')


url = 'http://httpbin.org/get'
data = {'key': 'value', 'abc':'xyz'}
response = requests.get(url,data)
print(response.text)
url = 'http://httpbin.org/post'
response1 = requests.post(url,data)
if response1.status_code ==200:
    print(response1.json())
else:
    print('fail')
print('##############')
"""
header = {
    "Host": "co.xiaoduoai.com",
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36',
    'Cookies': 'gr_user_id=91c30e5e-ff42-479b-a07d-7f09ea5f3bba; sensorsdata2015jssdkcross=%7B%22%24device_id%22%3A%2217076544405a7a-06e557b7c0d152-313f69-2073600-17076544406bd5%22%2C%22distinct_id%22%3A%22hjahdsa%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22first_id%22%3A%2217076d1b7571ec-077751318ed09e-313f69-2073600-17076d1b758cda%22%7D; bd8d3288ba0d3a54_gr_cs1=5d0caa426f7d2600011e476e; bd8d3288ba0d3a54_gr_last_sent_cs1=5d0caa426f7d2600011e476e; grwng_uid=6f2d475d-24c0-422b-8c27-d21d53ae7059; UNIONBACK_SID=2c22bc1dc9fe4fa7ac3442a0c1abebad; sso_token=token:5ba1de80e8184437a7ecaa0c1262ceb8; sa_jssdk_2015_co_xiaoduoai_com=%7B%22distinct_id%22%3A%22%E6%B7%98%E5%8A%A8%E5%8A%9B%22%2C%22first_id%22%3A%221705135ae4480c-0cdb89caa0b332-313f69-2073600-1705135ae45319%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%7D'
}

data={'username':'淘动力','password':'123456'}
response2 = requests.get(url,data)
print(response2.json())




auth = ('test', '123456')

response = requests.get('http://192.168.199.107', auth=auth)

print(response.text)
"""

##获取cookies
# 7. 返回CookieJar对象:
cookiejar = response12.cookies

# 8. 将CookieJar转为字典：
cookiedict = requests.utils.dict_from_cookiejar(cookiejar)
print(cookiejar)
print(cookiedict)


print("###########################session")
##session
#1、创建session对象，可以保存cookie值
a = requests.session()
#2、处理headers
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
# 3. 需要登录的用户名和密码
json_data = {'username':'hjahdsa','password':'123456'}
# 4. 发送附带用户名和密码的请求，并获取登录后的Cookie值，保存在ssion里
b=a.post(url='https://mc.xiaoduoai.com/api/v1/account/login',json =json_data)
if b.status_code == 200:
    print(b.text)
    print(b.json())
    print('成功了')
    #return a
else:
    print('fail')
# 5. ssion包含用户登录后的Cookie值，可以直接访问那些登录后才可以访问的页面
response = a.get("http://mc.xiaoduoai.com/api/v1/abnormal/setting/list")
#6、打印响应内容
print(response.text)
if response.content:
    print(response.json())
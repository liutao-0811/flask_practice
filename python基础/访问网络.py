import urllib
from  urllib import request
from urllib.request import urlopen
from urllib.parse import urlencode
import requests
url='https://www.baidu.com'
response = request.urlopen(url,timeout=1)
print(response.read().decode('utf-8'))#指定格式

url='https://co.xiaoduoai.com/login'
data={'username':'xinghuan123','password':123456}
req_data=urlencode(data)#将字典类型的请求数据转变为url编码
res=urlopen(url+'?'+req_data)#通过urlopen方法访问拼接好的url
res=res.read().decode()#read()方法是读取返回数据内容，decode是转换返回数据的bytes格式为str


print(res)
"""
#处理post请求,如果传了data，则为post请求


url1='https://co-test2.xiaoduoai.com/login'
header = {
    "Host": "wangcai-test-qb.xiaoduoai.com",
    'cache-control': "no-cache",
    'postman-token': "aca0d047-6c63-5736-b13e-d11df9fe71e1"
}
data={'username':'淘动力','password':123456}
response = requests.post(url1,header=header,params=data)
if response.status_code == 200:
    print(response.text)
else:
    print("fail")
"""
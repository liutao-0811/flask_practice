import requests

user_url='http://127.0.0.1:8080/register'
data={'username':['xiaoxiao','mingming'],
      'password':'123'}

r = requests.post(user_url,data=data)
print(r.text)

add_url = 'http://127.0.0.1:8080/add'
json_data = {
      'a':1,
      'b':2
}

r2 =requests.post(add_url,json=json_data)
print(r2.status_code)
print(r2.text)
print(r2.headers)

print('##################')
add1_url = 'http://127.0.0.1:8080/add1'
json_data = {
      'a':1,
      'b':2
}
r3 = requests.post(add1_url,json=json_data)

print(r3.headers) #获取相应头
print(r3.text)#获取相应体，即json格式的数据
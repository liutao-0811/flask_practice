import requests
import json

class RunMain():
    def __init__(self,url,method,data=None):
        self.res = self.run_main(url,method,data)

    def send_post(self,url, data):
        res = requests.post(url=url, data=data)
        if res.content:
        #if res.status_code == 200:
            return res.json()
        else:
            print("请求失败")


    def send_get(self,url, data):
        res = requests.get(url=url, data=data)
        if res.content:
        #if res.status_code == 200:
            return res.json()
            #return json.dump(res.json(),indent=2,sort_keys=True)#格式化返回数据
        else:
            print("请求失败")

    def run_main(self,url,method,data=None):
        res = None
        if method == "GET":
            res = self.send_get(url,data)
        else:
            res = self.send_post(url,data)
        return res

if __name__ == '__main__':
    url = "https://www.baidu.com/home/msg/data/personalcontent"
    data = {"num": 8,
    "indextype": "manht",
    "_req_seqid": 3480504641,
    "asyn": 1,
    "t": 1590418265010,
    "sid": 31656_1430_31326_21085_31595_31673_31464_31321_30824,
           }
    run = RunMain(url,"GET",data)

    print(run.res)
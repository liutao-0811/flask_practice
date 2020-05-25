import os
import sys
import random
import json
import msgpack


from locust import HttpUser,TaskSet,task


class GoodsListTask(TaskSet):
    @task(1)
    def goods_list_task( self ):
        goods_data = {
            "bound_to_chart": "all",
            "cid": "",
            "goods_category_id": "",
            "keyword": "",
            "keyword_type": "title",
            "limit": 10,
            "skip": 0,
            "sort": "sold_quantity_desc",
            "status": 1
        }
        req = self.client.post("/api/admin/goods/v2/list", json=goods_data, verify=False, name="goods_list", catch_response=True)
        if req.status_code == 200:
            data = json.loads(req.text)
            err = data.get("error")
            if err:
                req.failure(str(err))
            else:
                req.success()
        else:
            req.failure('Failed!')


class GoodsList(HttpUser):
    weight = 10  # 权重
    task_set = GoodsListTask
    min_wait = 500
    max_wait = 2000


if __name__ == '__main__':
    os.system("locust -f pttest.py --host=https://wangcai-test-gz.xiaoduoai.com")
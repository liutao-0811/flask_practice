import unittest
from unittest01.base.request_demo import RunMain

class TestMethod(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls):
    #     print("类执行之前的方法")
    #
    # @classmethod
    # def tearDownClass(cls):
    #     print("类执行之后的方法")

    #每次方法之前执行
    def setUp(self):
        self.run = RunMain()


    def test_01(self):
        url = "https://www.baidu.com/home/msg/data/personalcontent"
        data = {"num": 8,
                "indextype": "manht",
                "_req_seqid": 3480504641,
                "asyn": 1,
                "t": 1590418265010,
                "sid": 31656_1430_31326_21085_31595_31673_31464_31321_30824,
                }
        
        res = self.run.run_main(url,"GET",data)
        self.assertEqual(res['errorCode'],1001,"测试失败")
        print(res)
        print("这是第一个测试")
    def test_02(self):
        print("这是第二个测试")

    #每次方法后执行
    def tearDown(self):
        print("finnesh")
if __name__ == '__main__':
    unittest.main()
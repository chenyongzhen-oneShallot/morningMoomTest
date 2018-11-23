#coding:utf-8
#@Time    : 2018/11/21 10:52
#@Author  : 陈勇臻
#@File    : mmtest.py


import unittest
import requests
import json
import HTMLTestRunner

class demo(unittest.TestCase):
    def test_demo1(self):
        url="http://xxx/crontable/collect/recon/query"
        data=None
        headers={"client":"web"}
        result = requests.get(url=url,data=data,headers=headers)
        #res = json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)
        print(result)
        print(type(result))
        print(result['status'])
        self.assertEqual(result['status'],0,"测试通过")


if __name__=="__main__":
    suite = unittest.TestSuite()
    suite.addTest(demo("test_demo1"))
    unittest.TextTestRunner().run(suite)
    file_path = "./report/test_report.html"

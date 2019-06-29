#coding:utf-8
#@Time    : 2018/11/21 11:37
#@Author  : 
#@File    : test_duizhang.py
import unittest
import requests
import json
import HTMLTestRunner


#TestCase类，所有测试用例类继承的基本类
class duizhang(unittest.TestCase):
    def test_duizhang(self):
        #函数名必须以test开头，因为凡是继承TestCase类的函数名必须以test开头
        url="http://xxx/crontable/collect/recon/query"
        data=None
        headers={"client":"web"}
        result = requests.get(url=url,data=data,headers=headers)
        #res = json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)
        print(result)
        print(type(result))
        code = result.status_code
        #print(result['status'])
        #self.assertEqual(result['status'],200,"测试通过")
        self.assertEqual(code, 200)

if __name__=="__main__":
    unittest.main()

    # suite = unittest.TestSuite()
    # suite.addTest(duizhang("test_duizhang"))
    # unittest.TextTestRunner().run(suite)
    # file_path = "./report/test_report.html"

#测试用例脚本
import unittest
import requests
import json
from api.login import loginAPI
from parameterized import parameterized
import app
def bulid():
    datas=[]
    path='../data/login.json'
    with open(path,'r',encoding='utf-8') as fd:
        json_data=json.load(fd)
        for data in json_data:
            login_data=data.get('login_data')
            status_code=data.get('status_code')
            success=data.get('suceess')
            code=data.get('code')
            message=data.get('message')
            datas.append((login_data,status_code,success,code,message))
    return datas
     
class login_test(unittest.TestCase):
    #前置处理
    def setUp(self):
        self.login_test=loginAPI()
    #定义测试用例
    @parameterized.expand(bulid())
    def test01_login(self,login_data,status_code,success,code,message):
        """
        1、调用登录接口登录
        2、进行断言
        """
        response=self.login_test.test_login(json=login_data)
        #断言
        self.assertEqual(status_code,response.json().status_code)
        self.assertEqual(success,response.json().get("success"))
        self.assertEqual(code,response.json().get("code"))
        self.assertIn(message,response.json().get("message"))
    #提取token信息
        app.token=response.json().get("data")
        

    
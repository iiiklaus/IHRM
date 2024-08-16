#根据API接口文档封装测试系统的接口
import requests
import app
class loginAPI:
    def __init__(self):
        self.url=app.base_url+'/api/sys/login'
    def test_login(self,login_data):
        return requests.post(url=self.url,json=login_data)

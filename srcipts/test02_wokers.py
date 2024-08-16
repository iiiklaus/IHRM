import unittest
import requests
import json
from api.wokers import works
#将测试用例封装
class wokers_test(unittest.TestCase):
        # 添加员工测试用例设计
    employee_id =None
    def setUp(self) :
        self.workes=works()
    def test01_add_employee(self):
        add_employee_data = {
            "username": "jack0709t0728066",   # 用户名唯一
            "mobile": "13212072866",           # 手机号唯一
            "timeOfEntry": "2020-07-09",
            "formOfEmployment": 1,
            "workNumber": "072866",            # 员工ID唯一性
            "departmentName": "销售",
            "departmentId": "1266699057968001024",
            "correctionTime": "2020-07-30T16:00:00.000Z"
        }

        # 获取响应结果
        response = self.workes.add_employee(add_employee_data=add_employee_data)
    

        # 断言
        self.assertEqual(200, response.status_code)
        self.assertEqual(True, response.json().get("success"))
        self.assertEqual(10000, response.json().get("code"))
        self.assertIn("操作成功", response.json().get("message"))

        # 提取员工ID
        wokers_test.employee_id = response.json().get("data").get("id")
        print(wokers_test.employee_id)

    # 修改员工测试用例设计
    def test02_update_employee(self):
        update_employee_data = {"username": "rose0728"}
        # 获取响应结果
        response = self.workes.update_employee(wokers_test.employee_id, update_data=update_employee_data)
        print(response.json())

        # 断言
        self.assertEqual(200, response.status_code)
        self.assertEqual(True, response.json().get("success"))
        self.assertEqual(10000, response.json().get("code"))
        self.assertIn("操作成功", response.json().get("message"))
    # 查询员工测试用例设计
    def test03_get_employee(self):
        # 获取响应结果
        response = self.workes.get_employee(wokers_test.employee_id)
        print(response.json())

        # 断言
        self.assertEqual(200, response.status_code)
        self.assertEqual(True, response.json().get("success"))
        self.assertEqual(10000, response.json().get("code"))
        self.assertIn("操作成功", response.json().get("message"))

    # 删除员工测试用例设计
    def test04_delete_employee(self):
        # 获取响应结果
        response = self.workes.delete_employee(wokers_test.employee_id)
        print(response.json())

        # 断言
        self.assertEqual(200, response.status_code)
        self.assertEqual(True, response.json().get("success"))
        self.assertEqual(10000, response.json().get("code"))
        self.assertIn("操作成功", response.json().get("message"))

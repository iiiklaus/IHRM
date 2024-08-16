#封装添加员工接口 将请求进行封装
import app
import requests
class works:
    def __init__(self):
        self.url_add=app.base_url+"/api/sys/user"
        self.url_update_employee = app.base_url + "/api/sys/user/{}"
        self.url_get_employee = app.base_url + "/api/sys/user/{}"
        self.url_delete_employee = app.base_url + "/api/sys/user/{}"

    # 员工添加 post
    def add_employee(self, add_employee_data):
        return requests.post(url=self.url_add, json=add_employee_data, headers=app.headers_data)

    # 员工修改 put
    def update_employee(self, employee_id, update_data):
        # param={
        #     'targer':employee_id
        # }
        # requests.put(url=self.url_update_employee,json=update_data,params=param,headers=app.headers_data)
        url = self.url_update_employee.format(employee_id)
        return requests.put(url=url, json=update_data, headers=app.headers_data)
    # 员工查询 get
    def get_employee(self, employee_id):
        url = self.url_update_employee.format(employee_id)
        return requests.get(url=url, headers=app.headers_data)

    # 员工删除 delete
    def delete_employee(self, employee_id):
        url = self.url_update_employee.format(employee_id)
        return requests.delete(url=url, headers=app.headers_data)

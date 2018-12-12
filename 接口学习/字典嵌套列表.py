dict_data = {
  "code": "0",
  "data": {
    "token": {
      "id": "c9c4ec3e02814abfb5a696c84dfa1e1d",
      "user": {
        "account": "admin",
        "create": None,
        "description": None,
        "email": "12306@16.com",
        "id": "0a3913d4335049cb8a1586f1d1af238f",
        "modified": None,
        "name": "超级管理员",
        "password": "21232f297a57a5a743894a0e4a801fc3",
        "phone": "13333333333",
        "role": {
          "authority": None,
          "create": None,
          "createTime": None,
          "description": "系统超级管理员",
          "id": "001",
          "modified": None,
          "name": "超级管理员",
          "permissionIds": None,
          "type": "0"
        },
        "roleId": "001",
        "status": "1",
        "updateTime": "2017/7/28 12:00"
      }
    }
  },
  "message": "SUCCESS"
}

print(type(dict_data))
print(dict_data['data']['token']['id'])
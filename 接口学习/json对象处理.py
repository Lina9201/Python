from jsonpath_rw import parse
json_obj = {'code': '0', 'data': {'token': {'id': '6599b36c2685466f85522178c02b75d7', 'user': {'account': 'admin', 'create': None, 'description': None, 'email': '12306@16.com', 'id': '0a3913d4335049cb8a1586f1d1af238f', 'modified': None, 'name': '超级管理员', 'password': '21232f297a57a5a743894a0e4a801fc3', 'phone': '13333333333', 'role': {'authority': None, 'create': None, 'createTime': None, 'description': '系统超级管理员', 'id': '001', 'modified': None, 'name': '超级管理员', 'permissionIds': None, 'type': '0'}, 'roleId': '001', 'status': '1', 'updateTime': '2017/7/28 12:00'}}}, 'message': 'SUCCESS'}
jsonpath_expr = parse("data.token.id")
male = jsonpath_expr.find(json_obj)
print(male)
print([match.value for match in male])
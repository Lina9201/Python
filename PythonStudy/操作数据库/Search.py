import pymysql

# 打开数据库连接
db = pymysql.connect("172.50.10.60", "smart", "smart", "test", charset='utf8')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT * from EMPLOYEE")

# 查询数据库单条数据
data = cursor.fetchone()


print(data)

# 关闭数据库连接
db.close()


import pymysql

# 打开数据库连接
db = pymysql.connect("172.50.10.60", "smart", "smart", "test", charset='utf8')

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 使用 execute() 方法执行 SQL，如果表存在则删除
# cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# 使用预处理语句创建表
sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         INCOME FLOAT )"""

cursor.execute(sql)

# 关闭数据库连接
db.close()
import pymysql

# 打开数据库连接
db = pymysql.connect("172.20.15.13", "smart", "smart", "smart_dev", charset='utf8')

# 使用cursor()方法获取操作游标
cursor = db.cursor()
# SQL 插入语句
sql = """INSERT INTO disk(id, host_serial_number, type, vendor, model, serial_number, rotation_rate,
         name, create_time, microcode, disk_size, soft_delete, light_status)
         VALUES (2, 'other', 'Hitachi HUA722010CLA330', JPW9J0N10Y8DLV, '7200', '/dev/sdl', '2018-12-27 21:36:14', 'JP4OA3EA'
         '1000.2', '0', '0')"""

try:
   # 执行sql语句
   cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# 关闭数据库连接
db.close()

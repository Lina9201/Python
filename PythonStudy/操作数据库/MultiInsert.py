import pymysql

# 打开数据库连接
db = pymysql.connect("172.20.15.13", "smart", "smart", "smart_dev", charset='utf8')

# 使用cursor()方法获取操作游标
cursor = db.cursor()

for i in range(1, 2000):
    sql = """INSERT INTO disk(id, host_serial_number, type, vendor, model, serial_number, rotation_rate,
             name, crate_time, microcode, disk_size, soft_delete, light_status)
             VALUES (%d,'9800041200317517', 'HDD SATA', 'other', 'Hitachi HUA722010CLA330', 'JPW9J0N10Y8DLV', '7200', '/dev/sdl', '2018-12-27 21:36:14', 'JP4OA3EA',
         '1000.2', '0', '0')""" % (i)
    cursor.execute(sql)

db.commit()
db.close()

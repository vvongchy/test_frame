import pymysql
mysql_conn = pymysql.connect(host= '127.0.0.1', port= 3306, user= 'root', password= '980929', db= 'test_frame')
# 使用cursor()方法获取操作游标
cursor = mysql_conn.cursor()

# SQL 插入语句
sql = """INSERT INTO TEMP_DATA(name,value )
         VALUES ('Ma', 'Mohan')"""
try:
   # 执行sql语句
   cursor.execute(sql)
   # 提交到数据库执行
   mysql_conn.commit()
except:
   # Rollback in case there is any error
   mysql_conn.rollback()

# 关闭数据库连接
mysql_conn.close()
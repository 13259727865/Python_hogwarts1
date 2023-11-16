import pymysql

#连接数据库
db_con = pymysql.Connect(host='39.107.96.52',port=3307,database="lux_link",user="db_huaxia",password="EKZBLx9iJ6+WLVuN3FvE6w")
#创建游标
cur = db_con.cursor()
sql = "select * from pp_users"
#执行sql
cur.execute(sql)
#获取查询内容
# result = cur.fetchone()
# result = cur.fetchall()
result1 = cur.fetchmany(3)
print(result1)
cur.close()
db_con.close()
import pymysql
conn = pymysql.connect(host='212.129.255.189', port=3306,
                       user='root', password='FIk140!80',
                       database='mybatis', charset='utf8mb4')
try:
    # 2. 获取游标对象（Cursor）
    with conn.cursor() as cursor:
        # 3. 通过游标对象向数据库服务器发出SQL语句
        cursor.execute(
            'select * from tb_user'
        )
        row = cursor.fetchall()
        print(row)
except pymysql.MySQLError as err:
    # 4. 回滚事务
    conn.rollback()
    print(type(err), err)
finally:
    # 5. 关闭连接释放资源
    conn.close()
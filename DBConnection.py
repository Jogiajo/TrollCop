import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='pingu',
                             db='TrollCop',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

def insert_into_table():
    try:
        with connection.cursor() as cursor:
            cursor.execute("insert into user values('webmaster@python.org', 10)")
            connection.commit()
    finally:
        connection.close()

def retrieve_from_table(): 
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM `User`"
            cursor.execute(sql)
            result = cursor.fetchall()
            for i in result:
                print(i)
    finally:
        connection.close()

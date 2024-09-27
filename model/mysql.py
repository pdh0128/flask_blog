import pymysql

mysql_conn = pymysql.connect(
    host="localhost",
    port=3306,
    user='pdh0128',
    password="kdoornega0128",
    db="blog_db",
    charset="utf8"
)

def conn_mysqldb():
    if not mysql_conn.open:
        mysql_conn.ping(reconnect=True)
    return mysql_conn
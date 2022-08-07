from unittest import result
import pymysql

#데이터베이스 연결
MYSQL_HOST = 'localhost'
MYSQL_CONN = pymysql.connect(
    host=MYSQL_HOST,
    port=3306,
    user='blog',
    passwd='blog1234',
    db='blog_db',
    charset='utf8'
)

# 아래코드는 구독자 정보 확인 코드
# show=MYSQL_CONN.cursor()
# sql="SELECT * FROM user_info"
# show.execute(sql)
# results=show.fetchall()
# for x in results:
#     print(x)

#데이터베이스 재연결 함수
def conn_mysqldb():
    if not MYSQL_CONN.open:
        MYSQL_CONN.ping(reconnect=True)
    return MYSQL_CONN
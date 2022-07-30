from flask_login import UserMixin
from blog_model.mysql import conn_mysqldb

#flask_login모듈의 UserMixin클래스를 상속
class User(UserMixin):

    #아이디,이메일,블로그타입을 초기화
    def __init__(self, user_id, user_email, blog_id):
        self.id = user_id
        self.user_email = user_email
        self.blog_id = blog_id
    #사용자 아이디를 문자열 타입으로 리턴
    def get_id(self):
        return str(self.id)
    #사용자 아이디를 통해 사용자 객체를 가져오는 정적메서드
    @staticmethod
    def get(user_id):
        #mysql연결
        mysql_db = conn_mysqldb()
        db_cursor = mysql_db.cursor()
        #user_info테이블에서 사용자 아이디에 일치하는 정보를 가져오는 sql문
        sql = "SELECT * FROM user_info WHERE USER_ID = '" + str(user_id) + "'"
        # print (sql)
        db_cursor.execute(sql)
        user = db_cursor.fetchone()
        #찾는 사용자가 db에 없을 때 none리턴
        if not user:
            return None
        #찾는 사용자의 세 속성을 각 변수에 담아 객체 리턴
        user = User(user_id=user[0], user_email=user[1], blog_id=user[2])
        return user

    #사용자 이메일을 통해 사용자 객체를 가져오는 정적메서드
    #위의 메서드와 인자외의 다른부분은 동일
    @staticmethod
    def find(user_email):
        mysql_db = conn_mysqldb()
        db_cursor = mysql_db.cursor()
        sql = "SELECT * FROM user_info WHERE USER_EMAIL = '" + str(user_email) + "'"
        # print (sql)
        db_cursor.execute(sql)
        user = db_cursor.fetchone()
        if not user:
            return None
        
        user = User(user_id=user[0], user_email=user[1], blog_id=user[2])
        return user

    #이메일과 현재 보고있는 블로그 타입을 통해 사용자 생성(구독기능)
    @staticmethod
    def create(user_email, blog_id):
        #현재 사용자가 등록되어있는지 find메서드를 통해 확인
        user = User.find(user_email)
        #만약 사용자가 없을 경우 새로 사용자 생성
        if user == None:
            mysql_db = conn_mysqldb()
            db_cursor = mysql_db.cursor()
            #user_info테이블에 이메일과 블로그 타입을 값으로 튜플 생성
            sql = "INSERT INTO user_info (USER_EMAIL, BLOG_ID) VALUES ('%s', '%s')" % (str(user_email), str(blog_id))
            db_cursor.execute(sql)
            mysql_db.commit()
            #생성 후 find메서드를 통해 유저 객체 리턴
            return User.find(user_email)
        #만약 사용자가 이미 등록되어 있다면 바로 사용자 객체 리턴
        else:
            return user
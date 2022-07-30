from blog_model.mongodb import conn_mongodb
from datetime import datetime

#블로그 세선 관리 클래스
class BlogSession():
    #블로그 타입에 따라 html파일을 지정하는 딕셔너리
    blog_page = {'A': 'blog_A.html', 'B': 'blog_B.html'}
    session_count = 0

    #세션정보를 mongodb에 로그로 저장하는 메서드
    @staticmethod
    def save_session_info(session_ip, user_email, webpage_name):
        #접속 시간을 now_time에 담음
        now = datetime.now()
        now_time = now.strftime("%d/%m/%Y %H:%M:%S")  # https://strftime.org/

        #mongodb에 세션ip,사용자이메일,웹페이지이름,접속시간을 로그형식으로 저장
        mongo_db = conn_mongodb()
        mongo_db.insert_one({
            'session_ip': session_ip,
            'user_email': user_email,
            'page': webpage_name,
            'access_time': now_time
        })

    #블로그 id에 맞는 페이지(A or B)를 불러오는 메서드
    @staticmethod
    def get_blog_page(blog_id=None):
        #저장된 블로그 id가 없을 때(A,B를 번갈아 보여줌)
        if blog_id == None:
            #세션 카운트가 0일때 1로 변경해주고 A를 리턴
            if BlogSession.session_count == 0:
                BlogSession.session_count = 1
                return 'blog_A.html'
            else:
            #세션 카운트가 1일때 다시 0으로 변경해주고 B를 리턴
                BlogSession.session_count = 0
                return 'blog_B.html'
        #블로그 id가 존재할때, 즉 구독중일 때 blog_page딕셔너리에 해당하는 페이지를 리턴
        else:
            return BlogSession.blog_page[blog_id]

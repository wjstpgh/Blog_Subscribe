import pymongo

#pymongo연결
MONGO_HOST = 'localhost'
MONGO_CONN = pymongo.MongoClient('mongodb://%s' % (MONGO_HOST))

#연결 확인 메서드
def conn_mongodb():
    #연결시 연결객체 리턴
    try:
        MONGO_CONN.admin.command('ismaster')
        blog_ab = MONGO_CONN.blog_session_db.blog_ab
        # 아래코드는 접속로그 확인코드
        # all_data=blog_ab.find()
        # for data in all_data:
        #     print(data)
    #재연결
    except:
        MONGO_CONN = pymongo.MongoClient('mongodb://%s' % (MONGO_HOST))
        blog_ab = MONGO_CONN.blog_session_db.blog_ab
    return blog_ab


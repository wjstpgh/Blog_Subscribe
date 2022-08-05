from flask import Flask, jsonify, request, render_template, make_response, session
from flask_login import LoginManager, current_user, login_required, login_user, logout_user
from flask_cors import CORS
from blog_view import blog
from blog_control import user_mng
import os

# https 만을 지원하는 기능을 http 에서 테스트할 때 필요한 설정
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

app = Flask(__name__ , static_url_path='/static')
CORS(app)
#서버를 계속 열고있지 않으므로 세션이 리셋되는 것을 방지해 고정값을 줌(보안상 랜덤값으로 줘야하는 게 맞음)
app.secret_key = 'fixed_key'

app.register_blueprint(blog.blog_abtest, url_prefix='/blog')
login_manager = LoginManager()
login_manager.init_app(app)
#세션을 복잡하게 만듬
login_manager.session_protection = 'strong'

#db에서 아이디를 뽑아서 사용자 객체를 리턴
@login_manager.user_loader
def load_user(user_id):
    return user_mng.User.get(user_id)

#로그인되지 않는 사용자가 접근했을 때 접근부인
@login_manager.unauthorized_handler
def unauthorized():
    return make_response(jsonify(success=False), 401)

#모든 요청에 대해 IP값을 체크하고 세션에 저장되어있지 않다면 저장함
@app.before_request
def before_request():
    if 'client_id' not in session:
        session['client_id'] = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port='8080', debug=False)

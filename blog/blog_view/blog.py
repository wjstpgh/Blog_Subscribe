from flask import Flask, Blueprint, request, render_template, make_response, jsonify, redirect, url_for
import datetime
from blog_control.user_mng import User
from flask_login import current_user, login_user, logout_user

blog_abtest = Blueprint('blog', __name__)

@blog_abtest.route('/set_email', methods=['GET', 'POST'])
def set_email():
    #실제 form태그의 방식은 post방식을 사용, 아래 get은 연습용
    if request.method == 'GET':
        # print('set_email', request.headers)
        print('set_email', request.args.get('user_email'))
        # return redirect('/blog/test_blog')
        # return make_response(jsonify(success=True), 200)
        # 위의 두 리턴문과 비슷하게 다시 페이지 렌더링, 해당함수의 url로 리다이렉트
        return redirect(url_for('blog.test_a'))
    else:
        # print('set_email', request.headers)
        # content type이 application/json인 경우에만 아래처럼 바디를 가져올 수 있음
        # print('set_email', request.get_json())
        print('set_email', request.form['user_email'])
        #요천된 이메일과 페이지명을 기반으로 사용자 객체 생성(user_mng의 create메서드)
        user=User.create(request.form['user_email'], 'A')
        #사용자 객체를 통해 세션생성
        #30일간 로그인 세션정보 저장
        login_user(user, remember=True, duration=datetime.timedelta(days=30))
        #create메서드로 사용자 객체 생성후 다시 페이지 로드
        return redirect(url_for('blog.test_a'))

#구독취소 버튼시 세션정보 지우고 등록된 아이디 삭제
@blog_abtest.route('/logout')
def logout():
    User.delete(current_user.id)
    logout_user()
    return redirect(url_for('blog.test_a'))

#각 페이지 렌더 테스트경로
@blog_abtest.route('/a')
def test_a():
    #만약 사용자가 등록된 상태라면 html문서의 Jinja부분에 user_email을 넘겨줌
    if current_user.is_authenticated:
        return render_template('blog_A.html', user_email=current_user.user_email)
    #사용자 미등록 상태라면 user_email이 null인 html문서를 로드
    else:
        return render_template('blog_A.html')

@blog_abtest.route('/b')
def test_b():
    #create로 생성된 user객체로 login_user, id값으로 사용자등록
    #main의 load_user데코레이터 내부호출
    #load_user의 리턴 -> user_mng의 get메서드를 통해 사용자 반환
    #사용자가 반환된다면 아래 값이 true가 됨
    if current_user.is_authenticated:
        return render_template('blog_B.html', user_email=current_user.user_email)
    else:
        return render_template('blog_B.html')
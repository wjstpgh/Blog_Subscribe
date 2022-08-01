from flask import Flask, Blueprint, request, render_template, make_response, jsonify, redirect, url_for

from blog.blog_control.user_mng import User

blog_abtest = Blueprint('blog', __name__)


@blog_abtest.route('/set_email', methods=['GET', 'POST'])
def set_email():
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
        user=User.create(request.form['user_email'], 'A')
        return redirect(url_for('blog.test_a'))

#각 페이지 렌더 테스트경로
@blog_abtest.route('/a')
def test_a():
    return render_template('blog_A.html')

@blog_abtest.route('/b')
def test_b():
    return render_template('blog_B.html')

from flask import Flask, Blueprint, request, render_template, make_response, jsonify, redirect, url_for

blog_abtest = Blueprint('blog', __name__)


@blog_abtest.route('/set_email', methods=['GET', 'POST'])
def set_email():
    if request.method == 'GET':
        # print('set_email', request.headers)
        print('set_email', request.args.get('user_email'))
        return redirect(url_for('blog.test_a'))
    else:
        # print('set_email', request.headers)
        # content type 이 application/json 인 경우
        # print('set_email', request.get_json())
        print('set_email', request.form['user_email'])

        return redirect(url_for('blog.test_a'))

    # return redirect('/blog/test_blog')
    # return make_response(jsonify(success=True), 200)

@blog_abtest.route('/a')
def test_a():
    return render_template('blog_A.html')

@blog_abtest.route('/b')
def test_b():
    return render_template('blog_B.html')

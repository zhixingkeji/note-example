from flask import Flask, render_template, request, redirect, session

# 导包

# 创建对象
app = Flask(__name__)

# 加盐
app.secret_key = 'u2jksidjflsduwerjl'


USER_DICT = {
        '1': {'type': '医生', 'age': 18},
        '2': {'type': '警察', 'age': 28},
    }


# 路由装饰器
@app.route('/')
def root():
    return redirect('/home')


@app.route('/home')
def home():
    s = "一个字符串"  # 创建了一个字符串

    if request.method == 'GET':
        # 在hello.html中接受变量s
        return render_template("home.html", jay=s, user_dict=USER_DICT)


# 默认只能get请求，如果需要post请求要指定methods方法
@app.route('/login', methods=['GET', "POST"])
def login():
    # request.args  # 获取GET传来的值
    # request.form  # 获取POST传来的值

    u = request.form.get('username')
    p = request.form.get('pwd')

    if u == 'root' and p == 'root':
        # 放进了浏览器的cook里
        session['user_info'] = u
        return redirect('/user')
    else:
        return render_template("login.html", msg='密码错误')


@app.route('/logout')
def logout():
    del session["user_info"]
    return redirect('login')


@app.route('/user')
def user():
    user_info = session.get('user_info')
    if not user_info:
        return redirect('/login')
    return render_template("user.html")

@app.route('/detail')
def detail():
    user_info = session.get('user_info')
    if not user_info:
        return redirect('/login')

    uid = request.args.get('uid')
    info = USER_DICT.get(uid)
    return render_template("detail.html",info=info)


#开启调试
app.debug=True


# 主函数
if __name__ == '__main__':
    app.run()

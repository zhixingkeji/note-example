from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    # 在下面的代码行中使用断点来调试脚本。

    s = "一个字符串"  # 创建了一个字符串
    lista = ['医生', '教师', '警察']
    return render_template("hello.html", jay=s, caeer=lista)
    # 在hello.html中接受变量s


@app.route('/login', methods=['GET', "POST"])
def login():
    u = request.form.get('username')
    p = request.form.get('pwd')

    if u == 'root' and p == 'root':
        return '成功'
    else:
        return render_template("login.html")


if __name__ == '__main__':
    app.run(debug=True)

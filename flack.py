from flask import Flask
from flask import url_for, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def poem():
    with open("poem.txt", "r", encoding='utf-8') as f:
        content = f.read().split('\n')
    return render_template("poem.html", content=content)


@app.route('/stat')
def poem_stat():
    with open("poem_result.txt", "r", encoding='utf-8') as f_r:
        content = f_r.read().split('\n')
    return render_template("poem_result.html", content=content)


@app.route('/thanks')
def poem_thank():
    return 'Thank you!'


if __name__ == '__main__':
    app.run(debug=False)
from flask import Flask, render_template, redirect, url_for, request
from begin_func import search_begin

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('mainpage.html')

# поиск по русскому слову (Лиза)
@app.route('/rus_tr')
def rus_tr():
    return render_template('mainpage.html')

# поиск по табасаранскому слову (Настя К)
@app.route('/tab_tr')
def tab_tr():
    return render_template('mainpage.html')

# поиск по части  табасаранского слова (Настя Д)
@app.route("/begins", methods = ['GET'])
def login():
    return render_template('login.html')

@app.route("/start_results")
def search_start():
    args = request.args
    if args['nm']:
        if search_begin(args['nm']):
            return render_template('login.html', answers=search_begin(args['nm']))
        else:
            return render_template('login.html', go_back = 'Вашего слова нет в словаре')
    else:
        return render_template('login.html')

@app.route("/full_text")
def text():
    return render_template('begin_results.html', answers = search_begin(''))

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, url_for, redirect
import json
import flask_wtf

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
@app.route('/index')
def index():
    param = {}
    param['username'] = "Ученик Яндекс.Лицея"
    param['title'] = 'Домашняя страница'
    return render_template('index.html', **param)


nazv = 'Заготовка'


@app.route(f'/{nazv}')
def nazv():
    param = {}
    param['title'] = 'Заготовка'
    return render_template('base.html', **param)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

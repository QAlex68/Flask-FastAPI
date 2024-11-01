# Обработка GET запросов
from flask import Flask, url_for, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hi!'


@app.route('/get/')
def get():
    if level := request.args.get('level'):
        text = f'Похоже ты опытный игрок, раз имеешь уровень {level}<br>'
    else:
        text = 'Привет, новичок.<br>'
    return text + f'{request.args}'


if __name__ == '__main__':
    app.run(debug=True)

# ➢Создание таблиц в базе данных

from flask import Flask
from models_05 import db, User, Post, Comment   # Импортировать все модели таблиц которые должны появиться в базе

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


@app.route('/')
def index():
    return 'Hi!'


@app.cli.command("init-db")
def init_db():
    # показать ошибку с неверным wsqi.py
    db.create_all()
    print('OK')


if __name__ == '__main__':
    app.run(debug=True)

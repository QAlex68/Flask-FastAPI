# Работа с данными ➢Создание записей➢Изменение записей➢Удаление записей

from flask import Flask
from models_05 import db, User, Post, Comment  # Импортировать все модели таблиц которые должны появиться в базе

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


@app.route('/')
def index():
    return 'Hi!'


@app.cli.command("fill-db")
def fill_tables():
    count = 5
    # Добавляем пользователей
    for user in range(1, count + 1):
        new_user = User(username=f'user{user}', email=f'user{user}@mail.ru')
        db.session.add(new_user)
    db.session.commit()
    # Добавляем статьи
    for post in range(1, count ** 2):
        author = User.query.filter_by(username=f'user{post % count + 1}').first()
        new_post = Post(title=f'Post title {post}', content=f'Post content {post}', author=author)
        db.session.add(new_post)
    db.session.commit()


# @app.cli.command("init-db")
# def init_db():
#     db.create_all()
#     print('OK')
#
#
# @app.cli.command("add-john")
# def add_user():
#     user = User(username='john', email='john@example.com')
#     db.session.add(user)
#     db.session.commit()
#     print('John add in DB!')
#
#
# @app.cli.command("edit-john")
# def edit_user():
#     user = User.query.filter_by(username='john').first()
#     user.email = 'new_email@example.com'
#     db.session.commit()
#     print('Edit John mail in DB!')
#
#
# @app.cli.command("del-john")
# def del_user():
#     user = User.query.filter_by(username='john').first()
#     db.session.delete(user)
#     db.session.commit()
#     print('Delete John from DB!')


if __name__ == '__main__':
    app.run(debug=True)

# Создание моделей - Определение классов моделей - Создание связей между моделями
# ● Integer — целое число
# ● String — строка
# ● Text — текстовое поле
# ● Boolean — булево значение
# ● DateTime — дата и время
# ● Float — число с плавающей точкой
# ● Decimal — десятичное число
# ● Enum — перечисление значений
# ● ForeignKey — внешний ключ к другой таблице


from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    posts = db.relationship('Post', backref='author', lazy=True)  # Новая строка

    def __repr__(self):
        return f'User({self.username}, {self.email})'


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'Post({self.title}, {self.content})'

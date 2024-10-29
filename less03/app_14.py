# Flask-WTF - Настройка защиты от CSRF-атак
# Для установки Flask-WTF необходимо выполнить команду: pip install Flask-WTF

from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
# Генерация надежного секретного ключа
# >>> import secrets
# >>> secrets.token_hex()
app.config['SECRET_KEY'] = b'5f214cacbd30c2ae4784b520f17912ae0d5d8c16ae98128e3f549546221265e4'
csrf = CSRFProtect(app)


@app.route('/')
def index():
    return 'Hi!'


@app.route('/data/')
def data():
    return 'You data!'


@app.route('/form', methods=['GET', 'POST'])
@csrf.exempt
def my_form():
    ...
    return 'No CSRF protection!'


if __name__ == '__main__':
    app.run(debug=True)

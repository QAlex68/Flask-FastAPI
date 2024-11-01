# Обработка ошибок Декоратор errorhandler функция abort

import logging
from flask import Flask, url_for, render_template, request, abort

app = Flask(__name__)
logger = logging.getLogger(__name__)


@app.route('/')
def index():
    return 'Hi!'


@app.route('/blog/<int:id>')
def get_blog_by_id(id):
    # делаем запрос в БД для поиска статьи по id
    result = get_blog(id)
    if result is None:
        abort(404)


# возвращаем найденную в БД статью


@app.errorhandler(404)
def page_not_found(e):
    logger.warning(e)
    context = {
        'title': 'Страница не найдена',
        'url': request.base_url,
    }
    return render_template('404.html', **context), 404


def get_blog(id=None):
    return None


if __name__ == '__main__':
    app.run(debug=True)

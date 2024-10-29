# Замена route на get и post
from flask import Flask, url_for, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hi!'


@app.get('/submit')
def submit_get():
    return render_template('form.html')


@app.post('/submit')
def submit_post():
    name = request.form.get('name')
    return f'Hello {name}!'


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template
import platform
import datetime

app = Flask(__name__)

a = 10

# @app.route('/')
# def index():
#     return '<h1>Hello from Zerops!</h1> TEST5 {{a}}'

@app.route('/')
def home():
    fruits = ['apple', 'orange', 'pear', 'pineapple', 'durian']
    return render_template(
        'index.html',
        name='bob',
        age=40,
        fruits=fruits
    )


@app.route('/test')
def test():
    return 'test'


@app.route('/version')
def version():
    return platform.python_version()


app.run(host='0.0.0.0', port=8080)

from flask import Flask
import platform
import datetime

app = Flask(__name__)

a = 10

@app.route('/')
def index():
    return '<h1>Hello from Zerops!</h1> TEST5 {{a}}'


@app.route('/test')
def test():
    return 'test'


@app.route('/version')
def version():
    return platform.python_version()


app.run(host='0.0.0.0', port=8080)

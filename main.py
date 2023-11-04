from flask import Flask
import platform

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello from Zerops! TEST3'


@app.route('/test')
def test():
    return 'test'


@app.route('/version')
def version():
    return platform.python_version()


app.run(host='0.0.0.0', port=8080)

# from flask import Flask, render_template
# import platform
# import datetime

# app = Flask(__name__)

# # a = 10

# @app.route('/')
# def index():
#     return render_template('index.html', utc_dt=datetime.datetime.utcnow())

# # @app.route('/test')
# # def test():
# #     return 'test'


# # @app.route('/version')
# # def version():
# #     return platform.python_version()

# # from flask import Flask, render_template

# # app = Flask(__name__)

# # @app.route('/')
# # def home():
# #     return '<h1>Hello from Zerops!</h1> TEST5'

# app.run(host='0.0.0.0', port=8080)

import datetime
from flask import Flask
from flask import render_template
from flask import request

# app = Flask(__name__)
app = Flask(__name__, template_folder='templates')


@app.route('/')
def hello():
    fruits = ['apple', 'orange', 'pear', 'pineapple', 'durian']
    return render_template('index.html', utc_dt=datetime.datetime.utcnow(), fruits=fruits, args = request.args)

app.run(host='0.0.0.0', port=8080)

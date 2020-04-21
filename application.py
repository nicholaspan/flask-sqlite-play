# /usr/bin/python

import os

from . import database
from flask import Flask

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'app.sqlite')
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    @app.route('/')
    def hello_world():
        return 'Hello, World...'
    
    
    database.init_app(app)

    return app

"""
@app.route('/')
def hello_world():
    return 'Hello, World...'

@app.route('/blog')
def blog_handler():
    return 'TODO: Build out blog logic'

@app.route('login')
def login_handler():
    return 'TODO: Build out login logic'"""
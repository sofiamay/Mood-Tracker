from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask_oauthlib.client import OAuth

app = Flask(__name__)
app.config.from_object('config')
app.secret_key = '\xa4\xb9\x0b\x1dAM\xb6?\x82\x1c?\x90\x91\xea&X\xf2\x03\x9eT\xeb7A\xbe'
db = SQLAlchemy(app)

lm = LoginManager()
lm.init_app(app)

oauth = OAuth()


from app import views, models
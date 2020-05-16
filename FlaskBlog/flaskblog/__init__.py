from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = '51802a76ba3ee95ce4f7600cf416a2bacf9af7accdb71e8f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from flask_login import LoginManager
login_manager = LoginManager(app)	
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from flaskblog import routes
# routes are importing this file so that's why we import routes after created the app variable
# it must be create after app variable so that we don't face any circular import issue.
from flask import Flask
from config import Config
#import from sql alchemy and migrate
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
#import from flask login
from flask_login import LoginManager


app = Flask(__name__)

app.config.from_object(Config)
#sql alchemy and migrate initialization
db = SQLAlchemy(app)
migrate = Migrate(app, db)
#flask login initialization
login = LoginManager(app)
login.login_view = 'login'

from app import routes
from app import models #sqlalchemy + migrate


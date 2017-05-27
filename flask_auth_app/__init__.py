""" Initialize the package """

# pylint: disable=C0103,C0111,C0413,C0412

# The application
from flask_auth_app.application import create_app
app = create_app()
app.config.from_pyfile('config.py')


# The database
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)
from flask_auth_app.models import user


# The login manager
from flask_login import LoginManager
login_manager = LoginManager()
import flask_auth_app.models.login


# The views
from flask_auth_app import views

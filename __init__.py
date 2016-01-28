#################
#### imports ####
#################

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext bcrypt import BCrypt
import os

################
#### config ####
################

app = Flask(__name__)
bcrypt = BCrypt(app)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)
	
from project.users.views import users_blueprint

# register our blueprints
app.register_blueprint(users_blueprint)


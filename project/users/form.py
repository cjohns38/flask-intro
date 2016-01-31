from flask_wtf import Form 
from wtforms import TextField, PasswordField
from wtforms.validators import DataRequired

class LoginForm(Form):
    username = TextField('UserName', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])



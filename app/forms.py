from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Login', validators=[DataRequired()])
    password = PasswordField('Haslo', validators=[DataRequired()])
    remember_me = BooleanField('Zapamietaj mnie')
    submit = SubmitField('Zaloguj sie')
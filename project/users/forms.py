from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, EqualTo
from wtforms import ValidationError

from flask_login import current_user
from project.models import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('pass_confirm', message="Password MUST Match!!")])
    pass_confirm = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Register')
    def check_username(self, field):
        if User.query.filter_by(username = field.data).first():
            raise ValidationError('Your Username Has been Registered Already!')


class UpdateUserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('pass_confirm', message="Password MUST Match!!")])
    pass_confirm = PasswordField('Confirm Password', validators=[DataRequired()])

    def check_username(self, field):
        if User.query.filter_by(username = field.data).first():
            raise ValidationError('Your Username Has been Registered Already!')
    submit = SubmitField('Update')

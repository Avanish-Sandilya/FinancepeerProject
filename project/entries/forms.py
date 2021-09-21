from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField, validators
from wtforms.validators import DataRequired
from wtforms import ValidationError

class EntryForm(FlaskForm):
    file = FileField('Please Upload your Data File Here: ', validators=[DataRequired()])
    submit = SubmitField('Upload')

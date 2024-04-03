# Add any form classes for Flask-WTF here
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import InputRequired, DataRequired
from flask_wtf.file import FileField, FileAllowed

class  MovieForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    description = TextAreaField('Description', validators=[InputRequired()])
    poster = FileField('Poster', validators=[DataRequired(), FileAllowed(['jpg', 'png'], 'Photo')])
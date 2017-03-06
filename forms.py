from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired


class ArticleForm(FlaskForm):
    header = StringField('header', validators=[DataRequired()])
    signature = StringField('signature')
    body = TextAreaField('body', validators=[DataRequired()])

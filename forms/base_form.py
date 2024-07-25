from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, PasswordField
from wtforms.validators import DataRequired, Email, Length


class BaseForm(FlaskForm):

    def __init__(self):
        self.name_field = StringField(label='Name', validators=[DataRequired()])
        self.email_field = EmailField(lable='Email', validators=[DataRequired(), Email()])
        self.password_field = PasswordField(label='Password', validators=[DataRequired()])
        self.submit_field = SubmitField()
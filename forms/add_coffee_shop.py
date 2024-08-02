from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, BooleanField
from wtforms.validators import DataRequired, URL


class AddCoffeeShop(FlaskForm):
    name = StringField(label='Coffee name', validators=[DataRequired()])
    map_url = StringField(label='Map URL', validators=[DataRequired(), URL()])
    description = StringField(label='Coffee Description', validators=[DataRequired()])
    location = StringField(label='Location', validators=[DataRequired()])
    wifi = BooleanField(label='Wifi', default='')
    coffee = SelectField(label='Wifi', choices=[1, 2, 3, 4, 5], validators=[DataRequired()])
    power = SelectField(label='Wifi', choices=[1, 2, 3, 4, 5], validators=[DataRequired()])
    open = SelectField(label='Wifi', choices=[hour for hour in range(1, 12)], validators=[DataRequired()])
    close = SelectField(label='Wifi', choices=[hour for hour in range(1, 12)], validators=[DataRequired()])




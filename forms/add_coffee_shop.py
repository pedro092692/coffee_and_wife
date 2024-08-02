from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, BooleanField
from wtforms.validators import DataRequired, URL


class AddCoffeeShop(FlaskForm):
    name = StringField(label='Coffee name', validators=[DataRequired()])
    map_url = StringField(label='Map URL', validators=[DataRequired(), URL()])
    location = StringField(label='Location', validators=[DataRequired()])
    wifi = StringField(label='Wifi', choices=[1, 2, 3, 4, 5], validators=[DataRequired()])
    coffee = StringField(label='Wifi', choices=[1, 2, 3, 4, 5], validators=[DataRequired()])
    power = StringField(label='Wifi', choices=[1, 2, 3, 4, 5], validators=[DataRequired()])
    open = StringField(label='Wifi', choices=[hour for hour in range(1, 12)], validators=[DataRequired()])
    close = StringField(label='Wifi', choices=[hour for hour in range(1, 12)], validators=[DataRequired()])




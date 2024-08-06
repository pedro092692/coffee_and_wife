from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, BooleanField
from wtforms.validators import DataRequired, URL, Length


class AddCoffeeShop(FlaskForm):
    name = StringField(label='Coffee name', validators=[DataRequired()])
    map_url = StringField(label='Map URL', validators=[DataRequired()])
    description = StringField(label='Coffee Description', validators=[DataRequired(), Length(min=30, max=500)])
    wifi = BooleanField(label='Wifi', default='')
    power_socket = BooleanField(label='Power Socket', default='')
    quiet = BooleanField(label='Quiet', default='')
    coffee_service = BooleanField(label='Coffee Service', default='')
    food_service = BooleanField(label='Coffee Service', default='')
    credit_card_service = BooleanField(label='Coffee Service', default='')
    coffee = SelectField(label='Coffee score', coerce=int,
                         choices=[('0', 'Coffee Rating')] + [(f'{star}', f'{"⭐" * star}') for star in range(1, 6)],
                         validators=[DataRequired()])
    power = SelectField(label='Power score', coerce=int,
                        choices=[('0', 'Power Sockets Rating')] + [(f'{star}', f'{"⭐" * star}') for star in range(1, 6)],
                         validators=[DataRequired()])
    wifi_score = SelectField(label='Wifi score', coerce=int,
                        choices=[('0', 'WIFI Rating')] + [(f'{star}', f'{"⭐" * star}') for star in range(1, 6)],
                         validators=[DataRequired()])
    open = SelectField(label='Open', choices=[('', 'Open')] + [(f'{hour} AM', f'{hour} AM') for hour in range(1, 13)],
                       validators=[DataRequired()])
    close = SelectField(label='Open', choices=[('', 'Close')] + [(f'{hour} PM', f'{hour} PM') for hour in range(1, 13)],
                       validators=[DataRequired()])

    image_url = StringField(label='Image URL', validators=[DataRequired(), URL()])

    submit = SubmitField(label='Add Coffee Shop')


class Comment(FlaskForm):
    comment = TextAreaField(label='Comment', validators=[DataRequired(), Length(min=10, max=500)])
    submit = SubmitField(label='Post Comment')




from flask import Flask, url_for, redirect, render_template, request, flash
from flask_wtf.csrf import CSRFProtect
from database import Database
from dotenv import load_dotenv
from flask_security import login_required
from forms.add_coffee_shop import AddCoffeeShop
import os

# todo import data base
# todo add user table to data base
# todo create html template
# todo add flask security
# todo create crud for coffees


# load env
load_dotenv()

app = Flask(__name__)

# setup app
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
csfr = CSRFProtect(app)
# flask security
app.config['SECURITY_REGISTERABLE'] = True
app.config['SECURITY_SEND_REGISTER_EMAIL'] = False

# database
db = Database(app)
db.create_tables()


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/login')
def login():
    user = 'pedro bastidas'
    pedro = 'pedro pedro'
    return render_template('security/login_user.html', username=user, pedro=pedro)


@app.route('/register')
def register():
    return render_template('security/register_user.html')


@app.route('/coffee/<slug>', methods=['GET'])
def show_coffee(slug):
    return render_template('coffee.html')


@app.route('/add', methods=['GET', 'POST'])
@login_required
def add_coffee():
    form = AddCoffeeShop()

    if form.validate_on_submit():

        # Coffee Info
        coffee_name = form.name.data
        address_url = form.map_url.data
        description = form.description.data
        stable_wife = form.wifi.data
        power_sockets = form.power_sockets
        quiet = form.quiet.data
        coffee_service = form.coffee_service.data
        food_service = form.food_service.data
        credit_card = form.credit_card_service.data
        coffee_rating = form.coffee.data
        wifi_rating = form.wifi_score.data
        power_sockets_rating = form.power.data
        open_hour = form.open.data
        close_hour = form.close.data
        image_url = form.image_url.data

    return render_template('add.html', form=form)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


if __name__ == "__main__":
    app.run(debug=True)


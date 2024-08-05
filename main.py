from flask import Flask, url_for, redirect, render_template, request, flash
from flask_wtf.csrf import CSRFProtect
from database import Database
from dotenv import load_dotenv
from flask_security import login_required
from forms.add_coffee_shop import AddCoffeeShop
from flask_migrate import Migrate
from helpers import sanitize_iframe
from datetime import datetime
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

# flask migrate
migrate = Migrate(app, db.db, render_as_batch=True)


@app.route('/', methods=['GET'])
def home():
    coffees = db.get_all_coffee_shop()
    best = []
    if coffees:
        best = db.best_coffee_shop()[0][0]
    return render_template('index.html', coffees=coffees, best=best)


@app.route('/login')
def login():
    return render_template('security/login_user.html')


@app.route('/register')
def register():
    return render_template('security/register_user.html')


@app.route('/coffee/<slug>', methods=['GET', 'POST'])
def show_coffee(slug):
    coffee_shop = db.get_coffee_shop(slug=slug)
    return render_template('coffee.html', coffee_shop_info=coffee_shop)


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
        power_socket = form.power_socket.data
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

        iframe = sanitize_iframe(address_url)
        if not iframe:
            form.map_url.errors.append('Invalid iframe Only google maps iframe allowed.')
        else:
            new_coffee = db.add_new_coffee_shop(
                name=coffee_name,
                address_url=address_url,
                description=description,
                stable_wife=stable_wife,
                power_sockets=power_socket,
                quiet=quiet,
                coffee_service=coffee_service,
                food_service=food_service,
                credit_card=credit_card,
                coffee_score=coffee_rating,
                wifi_score=wifi_rating,
                power_sockets_score=power_sockets_rating,
                open_hour=open_hour,
                close_hour=close_hour,
                image_url=image_url

            )
            return redirect(url_for('show_coffee', slug=new_coffee.slug))

    return render_template('add.html', form=form)


@app.context_processor
def date():
    current_year = datetime.now().year
    return {'current_year': current_year}


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


if __name__ == "__main__":
    app.run(debug=True)


from flask import Flask, url_for, redirect, render_template, request, flash, abort
from flask_wtf.csrf import CSRFProtect
from database import Database
from dotenv import load_dotenv
from flask_security import login_required, current_user
from forms.add_coffee_shop import AddCoffeeShop, Comment
from flask_migrate import Migrate
from helpers import sanitize_iframe
from datetime import datetime
from flask_gravatar import Gravatar
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

# plugins
gravatar = Gravatar(
    app=app,
    size=100,
    rating='g',
    default='retro',
    force_default=False,
    use_ssl=False,
    base_url=None,
)


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
    form = Comment()

    if form.validate_on_submit():

        if not current_user.is_authenticated:
            return redirect('/')

        comment = form.comment.data

        # check if this user has comments
        if current_user.comments:
            db.update_comment(current_user.comments, comment)
        else:
            # add comment to db
            db.add_comment(
                user_id=current_user.id,
                cafe_id=coffee_shop.id,
                comment=comment
            )

        return redirect(url_for('show_coffee', slug=slug, _anchor='reviews'))

    return render_template('coffee.html', coffee_shop_info=coffee_shop, form=form)


@app.route('/all-coffee-shop', methods=['GET'])
def show_all():
    coffee_number = db.coffee_number()
    coffees = db.get_all_coffee_shop()
    return render_template('all_coffee.html', coffee_number=coffee_number, coffees=coffees)

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
                image_url=image_url,
                user_id=current_user.id

            )
            return redirect(url_for('show_coffee', slug=new_coffee.slug))

    return render_template('add.html', form=form)


@app.route('/edit/<slug>', methods=['GET', 'POST'])
@login_required
def edit_coffee(slug):
    coffee_info = db.get_coffee_shop(slug)

    if coffee_info.author.id != current_user.id:
        return redirect('/')

    form = AddCoffeeShop()

    if form.submit.data and form.validate():
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

        db.edit_cafe(
            cafe=coffee_info,
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

        return redirect(url_for('show_coffee', slug=coffee_info.slug))

    form.name.data = coffee_info.name
    form.map_url.data = coffee_info.map_url
    form.description.data = coffee_info.description
    form.wifi.data = coffee_info.wifi
    form.power_socket.data = coffee_info.power
    form.quiet.data = coffee_info.quiet
    form.coffee_service.data = coffee_info.coffee
    form.food_service.data = coffee_info.food
    form.credit_card_service.data = coffee_info.credit_card
    form.coffee.data = coffee_info.coffee_rating
    form.wifi_score.data = coffee_info.wifi_rating
    form.power.data = coffee_info.power_rating
    form.open.data = coffee_info.open
    form.close.data = coffee_info.close
    form.image_url.data = coffee_info.image_url

    return render_template('add.html', form=form)


@app.route('/delete-coffee/<slug>', methods=['GET', 'POST'])
@login_required
def delete_coffee(slug):
    if request.method == 'GET':
        return redirect(url_for('home'))

    coffee = db.get_coffee_shop(slug)
    db.delete_coffe(coffee)
    return redirect('/')


@app.route('/delete-comment/<comment_id>/<slug>', methods=['GET', 'POST'])
def delete_comment(comment_id, slug):
    if request.method == 'GET':
        return redirect(url_for('home'))

    db.delete_comment(comment_id)

    return redirect(url_for('show_coffee', slug=slug, _anchor='reviews'))


@app.context_processor
def date():
    current_year = datetime.now().year
    return {'current_year': current_year}


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


if __name__ == "__main__":
    app.run(debug=False)


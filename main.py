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


@app.route('/')
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


@app.route('/coffee/<slug>')
def show_coffee(slug):
    form = a
    return render_template('coffee.html')


@app.route('/add')
@login_required
def add_coffee():
    form = AddCoffeeShop()
    return render_template('add.html', form=form)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')



if __name__ == "__main__":
    app.run(debug=True)


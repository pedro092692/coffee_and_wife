from flask import Flask, url_for, redirect, render_template, request, flash
from flask_wtf.csrf import CSRFProtect
from database import Database
from dotenv import load_dotenv
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

# config app
app.config['SECURITY_REGISTERABLE'] = True

# database
db = Database(app)
db.create_tables()


@app.route('/')
def home():
    username = 'pedro092692'
    return render_template('index.html', user=username)


@app.route('/login')
def login():
    user = 'pedro bastidas'
    pedro = 'pedro pedro'
    return render_template('security/login_user.html', username=user, pedro=pedro)


@app.route('/register')
def register():
    return render_template('security/register_user.html')


if __name__ == "__main__":
    app.run(debug=True)


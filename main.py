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


# database
db = Database(app)
db.create_tables()

@app.route('/')
def home():
    username = 'pedro092692'
    return render_template('index.html', user=username)


if __name__ == "__main__":
    app.run(debug=True)


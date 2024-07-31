from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean, Float
from flask_security import Security, SQLAlchemyUserDatastore, hash_password
from flask_security.models import fsqla_v3 as fsqla
import os


# Create DB
class Base(DeclarativeBase):
    pass


# create extension=
db = SQLAlchemy(model_class=Base)
fsqla.FsModels.set_db_info(db)

#configure tables

class Role(db.Model, fsqla.FsRoleMixin):
    pass


class User(db.Model, fsqla.FsUserMixin):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(250), nullable=False)
    name: Mapped[str] = mapped_column(String(250), nullable=True)
    password: Mapped[str] = mapped_column(String(250), nullable=False)
    fs_uniquifier: Mapped[str] = mapped_column(String, nullable=False, unique=True)

class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    wifi: Mapped[float] = mapped_column(Float, nullable=False)
    coffee: Mapped[float] = mapped_column(Float, nullable=False)
    power: Mapped[float] = mapped_column(Float, nullable=False)
    open: Mapped[str] = mapped_column(String(250), nullable=False)
    close: Mapped[str] = mapped_column(String(250), nullable=False)

class Database:

    def __init__(self, app):
        self.db = db
        self.app = app

        # setup flask_security
        self.user_datastore = SQLAlchemyUserDatastore(db, User, Role)
        self.app.security = Security(self.app, self.user_datastore)

        # Database init
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///coffee_and_wifi.db'
        self.app.config['SECURITY_PASSWORD_SALT'] = os.environ.get('SECRET_KEY')

        self.db.init_app(self.app)

    def create_tables(self):
        with self.app.app_context():
            self.db.create_all()
            if not self.app.security.datastore.find_user(email=os.environ.get('EMAIL_FOR_LOGIN')):
                self.app.security.datastore.create_user(
                    email=os.environ.get('EMAIL_FOR_LOGIN'),
                    password=hash_password(os.environ.get('PASSWORD_FOR_LOGIN'))
                )
                self.db.session.commit()


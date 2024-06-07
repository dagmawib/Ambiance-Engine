from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __bind_key__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    Fname = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    country = db.Column(db.String(50), nullable=False)


class Cafe(db.Model):
    __bind_key__ = 'cafes'
    id= db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(205), unique = True)
    map_url= db.Column(db.String(250))
    img_url = db.Column(db.String(250))
    location = db.Column(db.String(250))
    seats = db.Column(db.Boolean)
    coffee_price = db.Column(db.Integer)
    has_sockets = db.Column(db.Boolean)
    has_toilet = db.Column(db.Boolean)
    has_wifi = db.Column(db.Boolean)
    can_take_calls = db.Column(db.Boolean)
    can_stay_long = db.Column(db.Boolean)
    is_quite = db.Column(db.Boolean)
    work_vibe = db.Column(db.Boolean)
    work_with_group = db.Column(db.Boolean)
    has_coffee = db.Column(db.Boolean)
    has_food = db.Column(db.Boolean)
    has_veggie = db.Column(db.Boolean)
    has_alcohol = db.Column(db.Boolean)
    accept_card = db.Column(db.Boolean)
    nice_lights = db.Column(db.Boolean)
    has_outdoor = db.Column(db.Boolean)
    is_spaciou = db.Column(db.Boolean)
    is_accessible = db.Column(db.Boolean)
    has_AC = db.Column(db.Boolean)
    pets_allowed = db.Column(db.Boolean)
    has_parking = db.Column(db.Boolean)
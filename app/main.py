from flask import Flask, render_template , request, Blueprint
from flask_sqlalchemy import SQLAlchemy
from . import db
from .models import Cafe

main_bp = Blueprint('main', __name__)



@main_bp.route('/')
def welcome():
    return render_template('welcome.html');

@main_bp.route('/home')
def home():
    all_cafes = db.session.query(Cafe).all()
    total_count =  len(all_cafes)
    filters = request.args.to_dict()
    
    if 'wifi' in filters:
        all_cafes = [cafe for cafe in all_cafes if cafe.has_wifi]
    if 'sockets' in filters:
        all_cafes = [cafe for cafe in all_cafes if cafe.has_sockets]
    if 'calls' in filters:
        all_cafes = [cafe for cafe in all_cafes if cafe.can_take_calls]
    if 'longStay' in filters:
        all_cafes = [cafe for cafe in all_cafes if cafe.can_stay_long]
    if 'tables' in filters:
        all_cafes = [cafe for cafe in all_cafes if cafe.seats]
    if 'quite' in filters:
        all_cafes = [cafe for cafe in all_cafes if cafe.is_quite]
    if 'workVibe' in filters:
        all_cafes = [cafe for cafe in all_cafes if cafe.work_vibe]
    if 'group' in filters:
        all_cafes = [cafe for cafe in all_cafes if cafe.work_with_group]
    if 'coffee' in filters:
        all_cafes = [cafe for cafe in all_cafes if cafe.has_coffee]
    if 'food' in filters:
        all_cafes = [cafe for cafe in all_cafes if cafe.has_food]
    if 'veggie' in filters:
        all_cafes = [cafe for cafe in all_cafes if cafe.has_veggie]
    if 'alcohol' in filters:
        all_cafes = [cafe for cafe in all_cafes if cafe.has_alcohol]
    if 'cards' in filters:
        all_cafes = [cafe for cafe in all_cafes if cafe.accept_card]
    if 'lights' in filters:
        all_cafes = [cafe for cafe in all_cafes if cafe.nice_lights]
    if 'outdoor' in filters:
        all_cafes = [cafe for cafe in all_cafes if cafe.has_outdoor]
    if 'spacious' in filters:
        all_cafes = [cafe for cafe in all_cafes if cafe.is_spaciou]
    if 'restroom' in filters:
        all_cafes = [cafe for cafe in all_cafes if cafe.has_toilet]
    if 'accessible' in filters:
        all_cafes = [cafe for cafe in all_cafes if cafe.is_accessible]
    if 'ac' in filters:
        all_cafes = [cafe for cafe in all_cafes if cafe.has_AC]
    if 'pets' in filters:
        all_cafes = [cafe for cafe in all_cafes if cafe.pets_allowed]
    if 'parking' in filters:
        all_cafes = [cafe for cafe in all_cafes if cafe.has_parking]
    remaining_count = len(all_cafes)
    return render_template("home.html", all_cafes=all_cafes, total_count = total_count,remaining_count=remaining_count , page = 'home' )

@main_bp.route("/cities")
def cities():
    return render_template("cities.html")

@main_bp.route('/suggestions')
def all_suggestion():
   return render_template('suggestion.html')

@main_bp.route('/contact')
def contact_us():
    return render_template('contact.html')

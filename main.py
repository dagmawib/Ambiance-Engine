from flask import Flask, render_template , request
from flask_sqlalchemy import SQLAlchemy
import csv
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cafes.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Cafe(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(205), unique = True)
    map_url= db.Column(db.String(250))
    img_url = db.Column(db.String(250))
    location = db.Column(db.String(250))
    has_sockets = db.Column(db.Boolean)
    has_toilet = db.Column(db.Boolean)
    has_wifi = db.Column(db.Boolean)
    can_take_calls = db.Column(db.Boolean)
    seats = db.Column(db.Integer)
    coffee_price = db.Column(db.Integer)

with app.app_context():
    db.create_all()

@app.route('/')
def welcome():
    return render_template("welcome.html")

@app.route('/home')
def home():
    all_cafes = db.session.query(Cafe).all()
    filters = request.args.to_dict()
    
    if 'wifi' in filters:
        all_cafes = [cafe for cafe in all_cafes if cafe.has_wifi]
    if 'sockets' in filters:
        all_cafes = [cafe for cafe in all_cafes if cafe.has_sockets]
    if 'calls' in filters:
        all_cafes = [cafe for cafe in all_cafes if cafe.can_take_calls]

    remaining_count = len(all_cafes)
    return render_template("home.html", all_cafes=all_cafes, remaining_count=remaining_count)


@app.route("/cities")
def cities():
    return render_template("cities.html")

if __name__ == "__main__":
    app.run(debug=True)
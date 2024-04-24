from flask import Flask, render_template
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

cafe_detail = []
@app.route('/')
def welcome():
    return render_template("welcome.html")

@app.route('/home')
def home():
    cafe_detail = db.session.query(Cafe).all()
    # print(cafe_detail)
    return render_template("home.html", all_cafes=cafe_detail)

@app.route("/cities")
def cities():
    return render_template("cities.html")

if __name__ == "__main__":
    app.run(debug=True)
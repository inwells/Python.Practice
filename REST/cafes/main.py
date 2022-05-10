from unicodedata import name
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        #Method 1. 
        dictionary = {}
        # Loop through each column in the data record
        for column in self.__table__.columns:
            #Create a new dictionary entry;
            # where the key is the name of the column
            # and the value is the value of the column
            dictionary[column.name] = getattr(self, column.name)
        return dictionary  

@app.route("/")
def home():
    return render_template("index.html")  

## HTTP GET - Read Record
@app.route("/random")
def random_cafe():
    cafes = db.session.query(Cafe).all()
    rand_cafe = random.choice(cafes)
    return jsonify(cafe=rand_cafe.to_dict())

@app.route("/all")
def all_cafes():
    cafes = db.session.query(Cafe).all()
    return jsonify(cafes=[cafe.to_dict() for cafe in cafes])

@app.route("/search")
def search_cafes():
    loc_query = request.args.get("loc").title()
    cafe_list = db.session.query(Cafe).filter_by(location=loc_query)
    count = cafe_list.count()
    if count == 1:
        return jsonify(cafe=cafe_list.to_dict())
    elif count > 1:
        return jsonify(cafes=[cafe.to_dict() for cafe in cafe_list])
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})

## HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def cafe_to_add():
    new_cafe=Cafe(
        name = request.form.get('name'),
        map_url = request.form.get('map_url'),
        img_url = request.form.get('img_url'),
        location = request.form.get('location'),
        seats = request.form.get('seats'),
        has_toilet = request.form.get('has_toilet'),
        has_wifi = request.form.get('has_wifi'),
        has_sockets = request.form.get('has_sockets'),
        can_take_calls = request.form.get('can_take_call'),
        coffee_price = request.form.get('coffee_price'),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})
## HTTP PUT/PATCH - Update Record
@app.route("/update-price/<cafe_id>", methods=["PATCH"])
def patch_price(cafe_id):
    new_price = request.args.get("new_price")
    cafe = db.session.query(Cafe).get(cafe_id)
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."}), 200
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404

## HTTP DELETE - Delete Record
@app.route("/close/<cafe_id>", methods=["DELETE"])
def close(cafe_id):
    api_key = request.args.get("api-key")
    cafe = db.session.query(Cafe).get(cafe_id)
    if api_key == "butteredtoast":
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(success={"success": "Successfully removed the cafe from the database"}), 200
        else:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404  
    else:
        return jsonify(error={"Forbidden": "Sorry, check yo' key please."}),403
if __name__ == '__main__':
    app.run(debug=True)

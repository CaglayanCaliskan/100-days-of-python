import random
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Cafe TABLE Configuration
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
        # Method 1.
        # dictionary = {}
        # # Loop through each column in the data record
        # for column in self.__table__.columns:
        #     # Create a new dictionary entry;
        #     # where the key is the name of the column
        #     # and the value is the value of the column
        #     dictionary[column.name] = getattr(self, column.name)
        # return dictionary

        # Method 2. Altenatively use Dictionary Comprehension to do the same thing.
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record

@app.route("/random")
def get_random_cafe():
    cafes = db.session.query(Cafe).all()
    random_cafe = random.choice(cafes)
    to_json = random_cafe.to_dict()
    return jsonify(cafe=to_json)


@app.route("/all")
def get_all_cafes():
    cafes = db.session.query(Cafe).all()
    return jsonify(cafes=[cafe.to_dict() for cafe in cafes])


@app.route("/search")
def find_cafes():
    query_location = request.args['loc']
    cafes = db.session.query(Cafe).filter_by(location=query_location).all()

    if cafes:
        return jsonify(cafes=[cafe.to_dict() for cafe in cafes])
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location"})

    # # or long way
    # cafes = db.session.query(Cafe).all()
    # arr = []
    # for cafe in cafes:
    #     arr.append(cafe.to_dict())
    # return jsonify(cafes=arr)


# HTTP POST - Create Record


@app.route("/add", methods=["GET", "POST"])
def add_cafe():
    # Add a new cafe
    # But dont forget unique=True from name key. Because you can add only 1 right now.
    # if you add again you need to delete it or change name value from postman

    if request.method == "POST":
        new_cafe = Cafe(
            name=request.form.get("name"),
            map_url=request.form.get("map_url"),
            img_url=request.form.get("img_url"),
            location=request.form.get("location"),
            has_sockets=bool(request.form.get("has_sockets")),
            has_toilet=bool(request.form.get("has_toilet")),
            has_wifi=bool(request.form.get("has_wifi")),
            can_take_calls=bool(request.form.get("can_take_calls")),
            seats=request.form.get("seats"),
            coffee_price=request.form.get("coffee_price"),
        )
        try:
            db.session.add(new_cafe)
            db.session.commit()
        except:
            return jsonify(error={f"Error": "Plese change name input.It is unique"})
        else:
            return jsonify(error={f"Succes": "Successfully added the new cafe."})

# HTTP PUT/PATCH - Update Record


@app.route("/update/<id>", methods=["GET", "PATCH"])
def cafe_update(id):
    if request.method == "PATCH":
        cafe = db.session.query(Cafe).get(id)
        new_price = request.form.get("new_price")
        try:
            cafe.coffee_price = new_price
            db.session.commit()
            return jsonify(response={"success": "Successfully updated the price."}), 200
        except:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404


# HTTP DELETE - Delete Record

@app.route("/report-closed/<id>", methods=["GET", "DELETE"])
def cafe_report(id):
    real_key = 321321
    if request.method == "DELETE":
        try:
            # catch params
            api_key_params = request.args['api-key']
            # conditions
            if (real_key == (int(api_key_params))):
                # do something on db
                cafe = db.session.query(Cafe).get(id)
                db.session.delete(cafe)
                db.session.commit()
                return jsonify(response={"success": "Successfully deleted the cafe from the database."}), 200

            else:
                return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403
        except:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404


if __name__ == '__main__':
    app.run(debug=True)

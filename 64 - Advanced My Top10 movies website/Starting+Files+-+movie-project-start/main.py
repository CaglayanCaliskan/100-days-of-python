from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

db = SQLAlchemy()
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Movie.db"
# initialize the app with the extension
db.init_app(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    year = db.Column(db.Integer, unique=True, nullable=False)
    description = db.Column(db.String)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String, nullable=False)
    img_url = db.Column(db.String, nullable=False)


class EditForm(FlaskForm):
    rating = FloatField('Your Rating Out of 10 e.g 7.5 Name')
    review = StringField('Your Review')
    submit = SubmitField(label='Update it')


# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )

# with app.app_context():
#     db.session.add(new_movie)
#     db.session.commit()


@app.route("/")
def home():
    myDb = db.session.execute(db.select(Movie)).scalars()
    data = []
    for item in myDb:
        data.append(item)

    return render_template("index.html", data=data)


@app.route("/edit/<id>", methods=['GET', 'POST'])
def edit(id):
    form = EditForm(request.form)
    if request.method == 'POST':
        with app.app_context():
            # find item
            item = db.get_or_404(Movie, id)
            # update from db
            item.rating = form.rating.data
            item.review = form.review.data

            db.session.commit()
        return redirect(url_for('home'))

    else:
        return render_template("edit.html", form=form)


@app.route("/delete/<id>")
def delete(id):
    with app.app_context():
        item = db.get_or_404(Movie, id)
        print(item)
        db.session.delete(item)
        db.session.commit()
        return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)

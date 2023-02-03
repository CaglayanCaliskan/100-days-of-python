from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db.init_app(app)


class NewBooks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    author = db.Column(db.String)
    review = db.Column(db.Float, nullable=False)


@app.route('/')
def home():
    all_books = db.session.execute(db.select(NewBooks)).scalars()
    # All book array need update
    with app.app_context():
        data = []
        for book in all_books:
            data.append(book)
    print("all book here: ", all_books)
    return render_template('index.html', data=data)


@app.route("/add",  methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        new_book = NewBooks(
            title=request.form["title"], author=request.form["author"], review=request.form["rating"])

        with app.app_context():
            db.session.add(new_book)
            db.session.commit()

        return redirect(url_for('home'))
    return render_template('add.html')


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0",
            port=5000)

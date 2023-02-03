# import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()

# # cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

# cursor.execute(
#     "INSERT INTO books VALUES(3, 'Test ss', 'caglayan', '8.5')")
# db.commit()

# db.close()


# create the extension
db = SQLAlchemy()
# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
# initialize the app with the extension
db.init_app(app)


class NewBooks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    author = db.Column(db.String)
    review = db.Column(db.Float, nullable=False)


new_book = NewBooks(

    title="Test3",
    author="J. K. Rowling",
    review=9.3
)


with app.app_context():
    all = db.session.execute(db.select(NewBooks)).scalars()
    print(type(all))
    arr = []
    for n in all:
        arr.append(n)
    print(arr)

    # db.session.add(new_book)
    # db.session.commit()

    # db.session.add(new_book)
    # db.session.commit()
    # db.create_all()

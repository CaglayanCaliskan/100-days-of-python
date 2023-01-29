from flask import Flask, render_template
import random
import datetime
import requests


app = Flask(__name__)


@app.route("/")
def home():
    current_year = datetime.datetime.now().year
    random_number = random.randint(1, 10)
    return render_template('index.html', num=random_number, year=current_year)


@app.route("/guess")
def guess_enter():
    return ("<h1> pls write your name on URL</h1> <br><p>/guess/name...</p>")


@app.route("/guess/<name>")
def guess(name):

    url = f"https://api.agify.io/?name={name}"
    url2 = f"https://api.genderize.io/?name={name}"
    response = requests.get(url)
    data = response.json()
    age = data['age']
    response2 = requests.get(url2)
    data2 = response2.json()
    gender = data2['gender']
    return render_template('guess.html', name=name.capitalize(), age=age, gender=gender)


@app.route("/blog/<num>")
def blog(num):
    print(num)
    url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url)
    data = response.json()
    return render_template('blog.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)

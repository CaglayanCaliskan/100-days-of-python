from flask import Flask, request
import random

app = Flask(__name__)

random_number = random.randrange(1, 10)
print(random_number)


def bolder(function):
    return f"<h1>{function}</h1>"


@app.route("/")
@bolder
def hello_world():
    return "<div style='text-align:center'>Guess a Number from url</div>"


@app.route("/<int:guess>")
def say_bye(guess):
    if (guess) > random_number:
        return "<h1>Too Big</h1>"
    elif (guess) == random_number:
        return "<h1>True guess</h1>"
    else:
        return "<h1>Too Low</h1>"


if __name__ == "__main__":
    app.run(debug=True)

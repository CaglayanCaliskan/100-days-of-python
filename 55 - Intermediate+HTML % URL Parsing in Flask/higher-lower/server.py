from flask import Flask, request
import random

app = Flask(__name__)

random_number = random.randrange(1, 10)
print(random_number)


@app.route("/")
def main():
    return "<h1 style='text-align:center'>Guess a Number between 1-9 url</h1>"\
        "<img src='https://media4.giphy.com/media/gl8ymnpv4Sqha/giphy.gif?cid=ecf05e473f9932625b469535b3be96c67fe9f35aa4bb9fc8&rid=giphy.gif&ct=g'></img>"


@app.route("/<int:guess>")
def result(guess):
    if guess > random_number:
        return "<h2>Too Much</h2>"
    elif guess < random_number:
        return "<h2>Too Low</h2>"
    else:
        return "<h1>You Win</h1>"


if __name__ == '__main__':
    app.run(debug=True)

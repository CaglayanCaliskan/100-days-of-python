import smtplib
from flask import Flask, render_template, request, redirect, url_for
import requests
import os
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)


response = requests.get("https://api.npoint.io/3d2bf53850f237d7bec8")
data = response.json()


def send_mail(obj):
    sender_email = "caliskancaglayan@gmail.com"
    receiver_email = "caosfreeman@example.com"
    password = os.getenv('GOOGLESMTP')
    message = f"Subject:Look Up {obj} \n This message is sent from Python."

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        print('Email sent!')
    except Exception as e:
        print('Something went wrong...', e)
    finally:
        server.quit()


@app.route("/")
def home():
    return render_template("home.html", data=data)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        print("post atıldı")
        user_name = request.form['name']
        user_email = request.form['email']
        user_phone = request.form['phone']
        user_message = request.form['message']
        mail_obj = f"User: {user_name} \n Email: {user_email} \n Phone: {user_phone}\n\n Message: \n {user_message}"
        send_mail(mail_obj)
        return redirect(url_for("success", usr=user_name))
    else:
        return render_template("contact.html")


@app.route("/success/<usr>")
def success(usr):
    return (f"<h1>Thank you {usr}. Message Send</h1>")


@app.route("/post")
def post():

    return render_template("post.html")


if __name__ == '__main__':
    app.run(debug=True)

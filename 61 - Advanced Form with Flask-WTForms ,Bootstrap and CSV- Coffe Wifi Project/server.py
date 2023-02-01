from flask import Flask, render_template, request, redirect, url_for
from wtforms import Form, SelectField, StringField, validators, PasswordField, SubmitField, DateTimeField
import pandas as pd
from save import save_to_csv


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/cafes',  methods=['GET', 'POST'])
def cafes():
    data = pd.read_csv('cafe-data.csv')
    leng = len(data) + 1
    df = data.iterrows()

    return render_template('cafes.html', data=data, df=df, len=leng)


class RegistrationForm(Form):
    cafe = StringField('Cafe Name')
    location = PasswordField('Location')
    open = StringField('Open at')
    close = StringField('Close at')
    coffee = SelectField('Coffe Quality', choices=[
                         "☕", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"])
    wifi = SelectField('Wifi Capacity', choices=["✘",
                                                 "💪", "💪💪", "💪💪💪", ])
    power = SelectField('Power', choices=["✘",
                                          "🔌", "🔌🔌", "🔌🔌🔌", ])
    submit = SubmitField(label='Add Cafe')


@app.route('/add',  methods=['GET', 'POST'])
def add():
    form = RegistrationForm(request.form)
    if request.method == 'POST':
        save_to_csv(cafe=form.cafe.data, location=form.location.data, open=form.open.data,
                    close=form.close.data, coffee=form.coffee.data, wifi=form.wifi.data, power=form.power.data)
        return redirect(url_for('cafes'))

    return render_template('add.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)

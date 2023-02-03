
from flask import Flask, render_template, redirect, request, url_for
from wtforms import Form, BooleanField, StringField, validators, PasswordField, SubmitField

app = Flask(__name__)


class RegistrationForm(Form):
    email = StringField(
        'Email', [validators.Length(max=30), validators.DataRequired()])
    password = PasswordField(
        'Password', [validators.Length(max=30), validators.DataRequired()])
    submit = SubmitField(label='Log in')
    # accept_rules = BooleanField('I accept the site rules', [
    #                             validators.InputRequired()])


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/success/<data>')
def success(data):
    print(data)
    return render_template('success.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        password = form.password.data
        email = form.email.data
        return redirect(url_for('success', data={"password": password, "email": email}))

    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, url_for, render_template
from wtforms import Form, BooleanField, TextField, PasswordField, validators
app = Flask(__name__)


class RegistrationForm(Form):
    username = TextField('Username'[validators.length(min=4, max=25)])
    email = TextFiled('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='passwords must match')
        ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.Required()])

@app.route('/register', methods['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.username.data, form.email.data, form.email.data,
            form.password.data)
        db_session.add(user)
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('register.html', form = form)

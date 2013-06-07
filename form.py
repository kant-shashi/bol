from wtforms import Form, BooleanField, TextField, PasswordField, validators


class RegistrationForm(Form):
	username = TextField('Username'[validators.length(min=4, max=25)])
	email = TextFiled('Email Address', [validators.Length(min=6, max=35)])
	password = PasswordField('New Password', [
		validators.Required(),
		validators.EqualTo('confirm', message='passwords must match')
		                                      ])
	confirm = PasswordField('Repeat Password')
	accept_tos = BooleanField('I accept the TOS', [validators.Required()])


from flask_wtf import FlaskForm, Form
from flask_login import current_user
from wtforms import StringField,SubmitField, BooleanField ,PasswordField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError
from flaskblog.models import User
class Registration(FlaskForm):
	"""docstring for Registration"""
	username = StringField('Username',
		validators = [DataRequired(),Length(min = 2, max = 20)])
	email = StringField('Email',validators = [DataRequired(), Email()])
	password = PasswordField('password',validators=[DataRequired()])
	confirm_password = PasswordField('confirm password',
									validators=[DataRequired(),EqualTo('password')])
	submit = SubmitField('Sign Up')

	def validate_username(self,username):
		user = User.query.filter_by(username=username.data).first()
		if user:
			raise ValidationError('username is taken please choose another one')
	def validate_email(self,email):
		user = User.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError('Email is taken please choose another one')


class Login(FlaskForm):
	"""docstring for Registration"""
	email = StringField('Email',validators = [DataRequired(), Email()])
	password = PasswordField('password',validators=[DataRequired()])
	remember = BooleanField('Remember Me')
	submit = SubmitField('Log In')

class UpdateAccountForm(FlaskForm):
	"""docstring for Registration"""
	username = StringField('Username',
		validators = [DataRequired(),Length(min = 2, max = 20)])
	email = StringField('Email',validators = [DataRequired(), Email()])
	submit = SubmitField('Update')

	def validate_username(self,username):
		if username.data != current_user.username:
			user = User.query.filter_by(username=username.data).first()
			if user:
				raise ValidationError('username is taken please choose another one')
	def validate_email(self,email):
		if email.data != current_user.email:
			user = User.query.filter_by(email=email.data).first()
			if user:
				raise ValidationError('Email is taken please choose another one')














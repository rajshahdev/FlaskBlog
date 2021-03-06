from flask import  request, render_template,url_for,flash,redirect
from flaskblog.forms import Registration, Login, UpdateAccountForm
from flaskblog import app,db,bcrypt
from flaskblog.models import  User, Post
from flask_login import login_user,current_user,logout_user,login_required

posts = [
	{
	'author' : 'Person',
	'title':'1st blog',
	'content':'first post', 
	'date_posted': 'May 17, 2020'
	},
	{
	'author' : 'Person',
	'title':'2nd Blog',
	'content':'Second post', 
	'date_posted': 'June 3, 2020'
	}

]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts = posts)

@app.route("/about")
def about():
	return render_template('about.html', title = 'About')

@app.route("/register", methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = Registration()
	if form.validate_on_submit():
		hashed_pwd = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = User(username=form.username.data,email=form.email.data,password=hashed_pwd)
		db.create_all()
		db.session.add(user)
		db.session.commit()
		flash(f'Account created !', 'success')
		return redirect(url_for('login'))
	return render_template('register.html',title='Register',form=form)
@app.route("/login",  methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = Login()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data): #user.password jo user ne enter kiya wo or form.password.data jo user ne registration k waqt enter kiya tha wo
			login_user(user,remember=form.remember.data)
			next_page = request.args.get('next')
			return redirect(next_page) if next_page else redirect(url_for('home'))
		else:
			flash('Login Unsuccessful. Please check email and password', 'danger')
	return render_template('login.html',title='Login',form=form)

@app.route("/logout")
def logout():
	logout_user()
	return redirect(url_for('home'))

@app.route("/account",  methods=['GET', 'POST'])
@login_required
def account():
	form=UpdateAccountForm()
	if form.validate_on_submit():
		current_user.username = form.username.data
		current_user.email = form.email.data
		db.session.commit()
		flash('Your account has been updated!', 'success')
		return redirect(url_for('account'))
	elif request.method == 'GET':
		form.username.data = current_user.username
		form.email.data = current_user.email
	image_file = url_for('static', filename = 'profile_pics/' + current_user.image_file)
	return render_template('account.html',title='Account', image_file = image_file, form=form)


























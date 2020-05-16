from datetime import datetime
from flaskblog import db,login_manager
from flask_login import UserMixin


#login_manager hai wo 1 type ka extension hai jo validate karta hai registration or login ko
@login_manager.user_loader 
def load_user(user_id):
	return User.query.get(int(user_id))

# here class user is same as User Table similarly Post Table. 


class User(db.Model, UserMixin):		
	id = db.Column(db.Integer,primary_key=True)
	username = db.Column(db.String(20),unique=True,nullable=False)
	email = db.Column(db.String(120),unique=True,nullable=False)
	image_file = db.Column(db.String(120), default='default.jpg',nullable=False)
	password  = db.Column(db.String(60),nullable=False)
	# -> 1 user many post so a one to many relationship
	posts = db.relationship('Post',backref='author',lazy=True) #backref is similar to add another column to the post model (when we have a post then we use backrep'author') && lazy is sqlalchemy load the data in 1 go.
	#posts is not a column its work in the background that the user have this much amount of post.
	def __repr__(self):
		return f"User('{self.username}','{self.email}', '{self.image_file}')"

class Post(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	title = db.Column(db.String(20))
	date_posted = db.Column(db.DateTime,nullable=False , default=datetime.utcnow)
	content = db.Column(db.Text, nullable = False)
	user_id = db.Column(db.Integer,db.ForeignKey('user.id'), nullable=False) #user_id is use to specify the user in the post model

	def __repr__(self):
		return f"Post('self.title', 'self.date_posted' )"
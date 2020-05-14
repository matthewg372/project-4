from flask import Flask, jsonify, g
import os
import models
from resources.users import users
from resources.profiles import profiles
from resources.to_do_lists import to_do_lists
from resources.friendships import friendships
from resources.posts import posts
from resources.meetings import meetings
from resources.comments import comments
from flask_login import LoginManager
from flask_cors import CORS 


DEBUG=True
PORT=8000

app = Flask(__name__)
app.secret_key = "ajhskdjasdhkasdjhkaiudhajugjhgdjhsgfhgjskdhjkfhjashd"
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
	try:
		return models.User.get_by_id(user_id)
	except models.DoesNotExist:
		return None

@login_manager.unauthorized_handler
def unauthorized():
	return jsonify(
		data={'error': 'user not logged in'},
		message="you must be logged in to do this",
		status=401
	),401

cors = CORS(users, origins=['http://localhost:3000'], supports_credentials=True)
cors = CORS(profiles, origins=['http://localhost:3000'], supports_credentials=True)
cors = CORS(to_do_lists, origins=['http://localhost:3000'], supports_credentials=True)
cors = CORS(friendships, origins=['http://localhost:3000'], supports_credentials=True)
cors = CORS(posts, origins=['http://localhost:3000'], supports_credentials=True)
cors = CORS(comments, origins=['http://localhost:3000'], supports_credentials=True)
cors = CORS(meetings, origins=['http://localhost:3000'], supports_credentials=True)


app.register_blueprint(users, url_prefix='/api/v1/users')
app.register_blueprint(profiles, url_prefix='/api/v1/profiles')
app.register_blueprint(to_do_lists, url_prefix='/api/v1/to_do_lists')
app.register_blueprint(friendships, url_prefix='/api/v1/friendships')
app.register_blueprint(posts, url_prefix='/api/v1/posts')
app.register_blueprint(comments, url_prefix='/api/v1/comments')
app.register_blueprint(meetings, url_prefix='/api/v1/meetings')


@app.before_request 
def before_request():
	print("you should see this before each request") 
	g.db = models.DATABASE
	g.db.connect()

@app.after_request 
def after_request(response):
	print("you should see this after each request") 
	g.db.close()
	return response 

@app.route('/')
def testing():
	return 'hello working'
	

if 'ON_HEROKU' in os.environ: 
	print('\non heroku!')
	models.initialize()

if __name__ == '__main__':
	models.initialize()
	app.run(debug=DEBUG, port=PORT)
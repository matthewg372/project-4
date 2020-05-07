from flask import Flask
import models
from resources.users import users
from resources.profiles import profiles
from resources.to_do_lists import to_do_lists
from resources.friendships import friendships
from flask_login import LoginManager


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






app.register_blueprint(users, url_prefix='/api/v1/users')
app.register_blueprint(profiles, url_prefix='/api/v1/profiles')
app.register_blueprint(to_do_lists, url_prefix='/api/v1/to_do_lists')
app.register_blueprint(friendships, url_prefix='/api/v1/friendships')
@app.route('/')
def testing():
	return 'hello working'


if __name__ == '__main__':
	models.initialize()
	app.run(debug=DEBUG, port=PORT)
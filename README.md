##WereHereToHelp - Models
```
class User(UserMixin, Model):
	username=CharField(unique=True)
	email=CharField(unique=True)
	password=CharField()
	class Meta:
		database = DATABASE

class Profile(Model):
	user=ForeignKeyField(User, backref='profiles')
	images=textField()
	first_name=Charfield()
	last_name=Charfield()
	days_sober=IntegerField()
	date=IntegerField()
	sponsor=BooleanField()
	date=DateTimeField(default=datetime.datetime.now)

class Friendship(Model):
	user1=ForeignKeyField(User, backref='friends')
	user2=ForeignKeyField(User, backref='friends')
	username=Charfield()

class Post(Model):
	user=ForeignKeyField(User, backref='posts')
	bio=Charfield()
	date=DateTimeField(default=datetime.datetime.now)

class Comment(Model):
	user=ForeignKeyField(User, backref='comments')
	post=ForeignKeyField(Post, backref='comments')
	bio=Charfield()

class Meeting(Model):
	date=Charfield()
	area=Charfield()
	info=Charfield()
	date=DateTimeField(default=datetime.datetime.now)
	class Meta:
		database = DATABASE

class ToDoItem(Model):
	user=ForeignKeyField(User, backref='ToDoList')
	item=Charfield()


```
```
#stretch goal

class Like(Model):
	user = ForeignKeyField(User, backref='likes')
	post = ForeignKeyField(Post, backref='likes')
	class Meta:
		database = DATABASE

class Message(Model):
	sender=ForeignKeyField(User, backref='sent_messages')
	receiver=ForeignKeyField(User, backref='received_messages')
	content=Charfield()
	Date=DateTimeField(default=datetime.datetime.now)


```

```
url              |	httpVerb| result
_____________________________________
/api/users/register| POST    | register a user
/api/users/login   | POST    | login user
/api/users/logout  | GET     | logout user
/api/users/<id>    | DELETE  | delete user

url              		|httpVerb | result
_____________________________________
/api/profile   		    | GET     | returns all profiles
/api/profile/    		| POST    | new profile created
/api/profile/<user_id>  | GET     | shows user profile
/api/profile/<id> 	    | Put     | update a profile
/api/profile/<id>       | DELETE  | delete profile

url              |	httpVerb| result
_____________________________________
/api/friendship/<id>| POST   | create a friendship
/api/friendship/<id>| DELETE | delete friendship



url              |	httpVerb| result
_____________________________________
/api/post/    | POST   | create a post
/api/post/    | GET    | get all posts
/api/post/<id>| PUT    | update a post
/api/post/<id>| DELETE | delete post

url                     |httpVerb | result
_____________________________________
/api/comments/<post_id> | POST    | create a comment
/api/comments/<post_id> | GET     | get all comments for a specific post
/api/comments/<id>      | PUT     | update a comment
/api/comments/<id>      | DELETE  | delete comment

url              |	httpVerb| result
_____________________________________
/api/meeting/    | POST   | create a meeting
/api/meeting/    | GET    | get all meetings
/api/meeting     | PUT    | update a meeting
/api/meeting/<id>| DELETE | delete meeting

url              |	httpVerb| result
_____________________________________
/api/todos/    | POST   | create a ToDo
/api/todos/    | GET    | get all items from to do list
/api/todos     | PUT    | update a ToDo
/api/todos/<id>| DELETE | delete ToDo
```
```
##StretchGoal

url              |	httpVerb| result
_____________________________________
/api/likes        | POST   | create like
/api/likes<id>    | GET    | find specific like to a post
/api/likes        | DELETE | delete like

```





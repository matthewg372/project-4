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
	first_Name=Charfield()
	Last_Name=Charfield()
	days_Sober=IntegerField()
	Age=IntegerField()
	Sponser=BooleanField()
	Date=DateTimeField(default=datetime.datetime.now)

class To_Do_List(Model):
	user=ForeignKeyField(User, backref='ToDoList')
	To_Do_Item=Charfield()

class Friend(Model):
	user=ForeignKeyField(User, backref='friends')
	username=Charfield()

class Post(Model):
	user=ForeignKeyField(User, backref='posts')
	Bio=Charfield()
	Date=DateTimeField(default=datetime.datetime.now)

class Comment(Model):
	user=ForeignKeyField(User, backref='comments')
	post=ForeignKeyField(Post, backref='comments')
	Bio=Charfield()


```
```
#stretch goal

class Like(Model):
	user = ForeignKeyField(User, backref='likes')
	post = ForeignKeyField(Post, backref='likes')
	likes=IntegerField()
	class Meta:
		database = DATABASE

class Messages(Model):
	Sender=Charfield()
	Receiver=Charfield()
	Content=Charfield()
	Date=DateTimeField(default=datetime.datetime.now)


```

```
url              |	httpVerb| result
_____________________________________
/api/users       | POST    | register a user
/api/users       | POST    | login user
/api/users       | GET     | logout user
/api/users/<id>  | DELETE  | delete user

url              		|httpVerb | result
_____________________________________
/api/profile   		    | GET     | returns all profiles
/api/profile    		| POST    | new profile created
/api/profile/users/<id> | GET     | shows users profile
/api/profile/<id> 	    | Put     | update a profile

url              |	httpVerb| result
_____________________________________
/api/friends     | POST   | create a friend
/api/friends/<id>| GET    | get all posts by user
/api/friends/<id>| DELETE | delete friend

url              |	httpVerb| result
_____________________________________
/api/ToDo     | POST   | create a ToDo
/api/ToDo/<id>| GET    | get all posts by user
/api/ToDo     | PUT    | update a ToDo
/api/ToDo/<id>| DELETE | delete ToDo


url              |	httpVerb| result
_____________________________________
/api/post     | POST   | create a post
/api/post/<id>| GET    | get all posts by user
/api/post     | PUT    | update a post
/api/post/<id>| DELETE | delete post

url              |	httpVerb| result
_____________________________________
/api/comments      | POST    | create a comment
/api/comments/<id> | GET     | get all comments for a specific post
/api/comments      | PUT     | update a comment
/api/comments/<id> | DELETE  | delete comment

```
```
##StretchGoal

url              |	httpVerb| result
_____________________________________
/api/likes        | POST   | create like
/api/likes<id>    | GET    | find specific like to a post
/api/likes        | DELETE | delete like

```





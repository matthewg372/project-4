from peewee import *

from flask_login import UserMixin
import datetime


DATABASE = SqliteDatabase('profiles.sqlite')

class User(UserMixin, Model):
	username=CharField(unique=True)
	email=CharField(unique=True)
	password=CharField()
	class Meta:
		database = DATABASE

class Profile(Model):
	user=ForeignKeyField(User, backref='profiles')
	images=TextField()
	first_Name=CharField()
	Last_Name=CharField()
	days_Sober=IntegerField()
	Age=IntegerField()
	Sponser=BooleanField()
	Friends=CharField()
	Date=DateTimeField(default=datetime.datetime.now)
	class Meta:
		database = DATABASE

class To_Do_List(Model):
	user=ForeignKeyField(User, backref='ToDoLists')
	To_Do_Item=CharField()
	class Meta:
		database = DATABASE

class Friend(Model):
	user=ForeignKeyField(User, backref='friends')
	username=CharField()
	class Meta:
		database = DATABASE

class Post(Model):
	user=ForeignKeyField(User, backref='posts')
	Bio=CharField()
	Date=DateTimeField(default=datetime.datetime.now)
	class Meta:
		database = DATABASE

class Comment(Model):
	user=ForeignKeyField(User, backref='comments')
	post=ForeignKeyField(Post, backref='comments')
	Bio=CharField()
	class Meta:
		database = DATABASE

def initialize():
	DATABASE.connect()
	DATABASE.create_tables([User, Profile, To_Do_List, Friend, Post, Comment], safe=True)
	print('connected to models and tables')
	DATABASE.close()
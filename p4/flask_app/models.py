from flask_login import UserMixin
from datetime import datetime
from . import db, login_manager
from mongoengine import ReferenceField, StringField, BinaryField, EmailField, FileField, ImageField, DateTimeField
from flask_wtf.file import FileRequired, FileAllowed
from .utils import current_time


# TODO: implement
@login_manager.user_loader
def load_user(user_id):
    return User.objects(username=user_id).first()

# TODO: implement fields
class User(db.Document, UserMixin):
    username = StringField(required=True, unique=True, min_length=1, max_length=40)
    email = EmailField(unique=True, required=True)
    password = StringField(required=True)
    profile_pic = db.ImageField()

    # Returns unique string identifying our object
    def get_id(self):
         return str(self.username)


# TODO: implement fields
class Review(db.Document):
    commenter = ReferenceField('User', required=True)
    content = StringField(required=True, min_length=5, max_length=500)
    date = DateTimeField(default=current_time)
    imdb_id = StringField(required=True, min_length=9, max_length=9)
    movie_title = StringField(required=True, min_length=1, max_length=100)
    image = db.StringField()
    #Uncomment when other fields are ready for review pictures
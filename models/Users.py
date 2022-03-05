from mongoengine import *
import jwt


class User(Document):
    name = StringField(max_length=50)
    email = StringField(max_length=120)

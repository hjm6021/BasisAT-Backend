from mongoengine import *


class User(Document):
    name = StringField(max_length=50)
    email = StringField(max_length=120)

    def generateToken():
        return "something"

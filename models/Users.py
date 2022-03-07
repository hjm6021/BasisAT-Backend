from enum import unique
from mongoengine import *
import jwt


class User(Document):
    username = StringField(max_length=50, required=True, unique=True)
    isAdmin = BooleanField(default=False, required=True)

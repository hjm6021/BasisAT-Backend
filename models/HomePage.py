from mongoengine import *


class HomePage(Document):
    description = StringField(required=True)

    meta = {"collection": "home"}

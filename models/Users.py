from mongoengine import *


class User(Document):
    username = StringField(max_length=50, required=True, unique=True)
    isAdmin = BooleanField(default=False, required=True)

    def registerIfNotExists(self):
        # if doesnt exist, create User
        if not User.objects.get(username=self.username):
            self.save()

        return User.objects.get(username=self.username)

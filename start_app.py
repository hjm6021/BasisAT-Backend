from flask import Flask
from flask_restful import Api
from urls import addResource
from mongoengine import connect
import config

app = Flask(__name__)


# connect to the database
connect(db=config.mongoDb, host=config.mongoHost, port=config.mongoPort)

api = Api(app)
addResource(api)

if __name__ == "__main__":
    app.run(host="0.0.0.0")

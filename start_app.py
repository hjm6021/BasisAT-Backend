from flask import Flask
from flask_restful import Api
from urls import addResource
from mongoengine import connect
import config

from flask_cors import CORS

app = Flask(__name__)
# hanlde CORS error. supports_credentials=True for Cookies
CORS(app, supports_credentials=True)

# connect to the database
connect(db=config.mongoDb, host=config.mongoHost, port=config.mongoPort)

api = Api(app)
addResource(api)

if __name__ == "__main__":
    app.run(host="127.0.0.1")

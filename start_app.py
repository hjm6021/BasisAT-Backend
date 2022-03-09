from flask import Flask
from flask_restful import Api
from mongoengine import connect
import config
from urls import addResource
from flask_cors import CORS
from flasgger import Swagger

app = Flask(__name__)
app.config.from_object(config)

app.config["SWAGGER"] = app.config["FLASGGER_SETTING"]

# hanlde CORS error. supports_credentials=True for Cookies
CORS(app, supports_credentials=True)

# connect to the database
connect(
    db=app.config["MONGODB"],
    host=app.config["MONGODB_HOST"],
    port=app.config["MONGODB_PORT"],
)

api = Api(app)
addResource(api)
swagger = Swagger(app, template=app.config["FLASGGER_TEMPLATE"])

if __name__ == "__main__":
    app.run(host="127.0.0.1")

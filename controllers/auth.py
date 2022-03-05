from unicodedata import name
from flask import request
from flask_restful import Resource
from config import jwtSecretKey, jwtAlgorithm
import requests
from lib import authAPI


class Login(Resource):
    def post(self):
        name = request.json.get("name")
        password = request.json.get("password")
        response = authAPI.login(name, password)
        print(response.headers)
        print(response.json())
        return "login successfully"


class Logout(Resource):
    def post(self):
        return {"type": "logout"}


class Check(Resource):
    def post(self):
        return {"type": "check"}

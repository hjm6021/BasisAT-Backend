from flask import abort, make_response, request
from flask_restful import Resource
from config import jwtSecretKey, jwtAlgorithm
from lib import authAPI
import jwt


def generateJwtToken(payload):
    jwtToken = jwt.encode(payload, jwtSecretKey, jwtAlgorithm)
    return jwtToken


class Login(Resource):
    def post(self):
        username = request.json.get("username")
        password = request.json.get("password")

        # Validate username and password parameters
        if not username or not password:
            abort(400)

        # Request to BLAS API for authentication and Abort 500 if there is error
        try:
            responseFromBLAS = authAPI.login(username, password)
        except:
            abort(500)

        # Abort 401 if response from BLAS API has error
        if responseFromBLAS.status_code != 200:
            abort(401)

        responseFromBLAS = responseFromBLAS.json()
        # Abort 401 if authentication failed
        if responseFromBLAS.get("error_code") != 0:
            abort(401)

        token = responseFromBLAS.get("records").get("token")

        # Generate JWT Token and Set cookies with JWT Token
        payload = {"username": username, "token": token}
        jwtToken = generateJwtToken(payload)

        response = make_response({"username": username})
        response.set_cookie(
            key="access-token",
            value=jwtToken,
            max_age=60 * 60 * 24 * 1,
            httponly=True,
        )

        return response


class Logout(Resource):
    def post(self):
        return {"type": "logout"}


class Check(Resource):
    def post(self):
        return {"type": "check"}

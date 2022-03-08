from urllib import response
from flask import abort, make_response, request
from flask_restful import Resource
from config import jwtSecretKey, jwtAlgorithm
from lib import authAPI
import jwt
from flasgger import swag_from


def generateJwtToken(payload):
    jwtToken = jwt.encode(payload, jwtSecretKey, jwtAlgorithm)
    return jwtToken


class Login(Resource):
    def post(self):
        """
        post endpoint
        ---
        tags:
          - Authentication
        parameters:
          - name: a
            in: query
            type: integer
            required: true
            description: first number
          - name: Cookie
            in: header
            type: integer
            required: true
            description: second number
        responses:
          500:
            description: Error The number is not integer!
          200:
            description: Number statistics
            schema:
              id: stats
              properties:
                sum:
                  type: integer
                  description: The sum of number
                product:
                  type: integer
                  description: The sum of number
                division:
                  type: integer
                  description: The sum of number
        """
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
        )

        return response


class Logout(Resource):
    def post(self):
        """
        post endpoint
        ---
        tags:
          - Authentication
        parameters:
          - name: a
            in: query
            type: integer
            required: true
            description: first number
          - name: b
            in: query
            type: integer
            required: true
            description: second number
        responses:
          500:
            description: Error The number is not integer!
          200:
            description: Number statistics
            schema:
              id: stats
              properties:
                sum:
                  type: integer
                  description: The sum of number
                product:
                  type: integer
                  description: The sum of number
                division:
                  type: integer
                  description: The sum of number
        """
        return "", 204


class Check(Resource):
    def get(self):
        """
        check JWT access-token
        ---
        tags:
          - Authentication
        parameters:
          - name: access-token
            in: header
            type: string
            required: true
        responses:
          401:
            description: Error - No JWT access-tokne in HTTP Header
          200:
            description: Number statistics
            schema:
              id: Users
              properties:
                username:
                  type: string
                  description: BLAS Username
        """
        jwtAccessToken = request.cookies.get("access-token")
        if jwtAccessToken is None:
            abort(401)

        decodedJwtAccessToken = jwt.decode(
            jwtAccessToken, jwtSecretKey, algorithms=[jwtAlgorithm]
        )
        del decodedJwtAccessToken["token"]

        return decodedJwtAccessToken

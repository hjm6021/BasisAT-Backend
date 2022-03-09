from flask import abort, make_response, request, current_app
from flask_restful import Resource
from lib import authAPI
import jwt


def generateJwtToken(payload):
    jwtToken = jwt.encode(
        payload,
        current_app.config["JWT_SECRET_KEY"],
        current_app.config["JWT_ALGORITHM"],
    )
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

        # Send a request to BLAS API for authentication and Abort 500 if there is error
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
            description: Error - No JWT access-token in HTTP Header
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
            jwtAccessToken,
            current_app.config["JWT_SECRET_KEY"],
            algorithms=[current_app.config["JWT_ALGORITHM"]],
        )
        del decodedJwtAccessToken["token"]

        return decodedJwtAccessToken

from flask import abort, make_response, request, current_app
from flask_restful import Resource
from lib import authAPI
import jwt
from models import User


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
        Login
        ---
        tags:
          - Authentication
        requestBody:
          required: true
          consumes:
            application/json:
        parameters:
          - name: body
            in: body
            required: true
            schema:
              required:
                - username
                - password
              properties:
                username:
                  type: string
                  description: BLAS Username
                password:
                  type: string
                  description: BLAS Password
        responses:
          400:
            description: no Username or Password in Request Body
          401:
            description: Authentication Failed
          200:
            description: Login Successfully
            schema:
              id: Users
              properties:
                username:
                  type: integer
                  description: BLAS username
                isAdmin:
                  type: boolean
                  description: is user administrator
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

        user = User(username=username).registerIfNotExists()

        # Generate JWT Token and Set cookies with JWT Token
        payload = {"username": username, "token": token}
        jwtToken = generateJwtToken(payload)

        response = make_response(user.to_json())
        response.set_cookie(
            key="access-token",
            value=jwtToken,
            max_age=60 * 60 * 24 * 1,
        )

        return response


class Logout(Resource):
    def post(self):
        """
        Logout
        ---
        tags:
          - Authentication
        responses:
          204:
            description: Login Successfully
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
            description: Check JWT Token Successfully
            schema:
              id: Users
              properties:
                username:
                  type: string
                  description: BLAS Username
                isAdmin:
                  type: boolean
                  description: check whether User is admin
        """
        jwtAccessToken = request.cookies.get("access-token")
        if jwtAccessToken is None:
            abort(401)

        decodedJwtAccessToken = jwt.decode(
            jwtAccessToken,
            current_app.config["JWT_SECRET_KEY"],
            algorithms=[current_app.config["JWT_ALGORITHM"]],
        )

        user = User.objects.get(username=decodedJwtAccessToken["username"])

        response = make_response(user.to_json())

        return response

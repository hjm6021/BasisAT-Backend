from flask_restful import Resource
from models import HomePage
from flask import make_response, request
from middlewares.checkJwtToken import checkJwtTokenMiddleware
from middlewares.isAdmin import isAdmin


class Home(Resource):
    @checkJwtTokenMiddleware
    def get(self):
        """
        Get Homepage Description
        ---
        tags:
          - HomePage
        parameters:
          - name: access-token
            in: header
            type: string
            required: true
        responses:
          401:
            description: Error - No JWT access-token in HTTP Header
          200:
            description: HomePage Description
            schema:
              id: HomePage
              properties:
                _id:
                    type: object
                description:
                  type: string
                  description: HomePage Description
        """
        home = HomePage.objects.get().to_json()
        response = make_response(home)
        return response

    @checkJwtTokenMiddleware
    @isAdmin
    def put(self):
        """
        Edit Homepage Description
        ---
        tags:
          - HomePage
        parameters:
          - name: access-token
            in: header
            type: string
            required: true
          - name: body
            in: body
            required: true
            schema:
              required:
                - id
                - editor
              properties:
                id:
                  type: string
                  description: Home Description ID
                editor:
                  type: markdown
                  description: The Description which needs to be updated
        responses:
          401:
            description: Error - No JWT access-token in HTTP Header
          403:
            description: Error - No Permission
          204:
            description: Edit HomePage Description Successfully
        """
        _id = request.json.get("id")
        editor = request.json.get("editor")

        HomePage.objects(pk=_id["$oid"]).update_one(set__description=editor)

        return "", 204

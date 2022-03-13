from controllers.auth import Login, Logout, Check
from controllers.home import Home


def addResource(api):
    # Authentication Routing
    api.add_resource(Login, "/auth/login")
    api.add_resource(Logout, "/auth/logout")
    api.add_resource(Check, "/auth/check")

    api.add_resource(Home, "/home")

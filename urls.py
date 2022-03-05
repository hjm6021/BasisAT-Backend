from controllers.auth import Login, Logout, Check


def addResource(api):
    # Authentication Routing
    api.add_resource(Login, "/auth/login")
    api.add_resource(Logout, "/auth/logout")
    api.add_resource(Check, "/auth/check")

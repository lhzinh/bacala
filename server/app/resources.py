from flask_restx import Resource

from app.extensions import api

user_ns = api.namespace("users", description="USER operations")


@user_ns.route("/")
class UserList(Resource):
    """Shows a list of all users"""

    @user_ns.doc("list_users")
    def get(self):
        """List all users"""
        return "Hello"


def init_namespaces(api):
    for space in [user_ns]:
        api.add_namespace(space)

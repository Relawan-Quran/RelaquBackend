import datetime
import traceback
from app.mod_api_v1 import response
from app.mod_api_v1.user_schema import LoginSchema, ns_user as api
from flask import request
from flask_restx import Resource
from flask_jwt_extended import (
    get_jwt_identity, jwt_required, create_access_token, create_refresh_token
)


@api.route("/login")
class LoginClass(Resource):
    @api.expect(LoginSchema)
    def post(self):
        try:
            args = api.payload
            username = args["username"]

            expires_delta = datetime.timedelta(hours=100)
            expires_delta_refresh = datetime.timedelta(weeks=3)
            access_token = create_access_token(
                str(username), expires_delta=expires_delta
            )
            refresh_token = create_refresh_token(
                str(username), expires_delta=expires_delta_refresh
            )
            return response.ok(
                {
                    "token": access_token,
                    "refresh_token": refresh_token
                },
                "Data available"
            )
        except Exception as e:
            print(e)
            print(traceback.format_exc())
            return response.bad("Error")


@api.route("/logout")
class LogoutClass(Resource):
    @jwt_required(locations=["headers"])
    def post(self):
        try:
            session_id = get_jwt_identity()
            print(str(session_id))

            return response.ok({}, "Ok")

        except Exception as e:
            print(e)
            print(traceback.format_exc())
            return response.bad("Error")

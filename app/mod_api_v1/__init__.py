from flask import Blueprint, request
from flask_restx import Api, apidoc
from flask_jwt_extended.exceptions import JWTExtendedException
from app.mod_api_v1 import response
from config import DEBUG
from app.mod_api_v1.user import api as user


doc = "/doc"
if DEBUG is False:
    doc = False
base_url = "/api/v1"

blueprint = Blueprint("api_v1", __name__, url_prefix=base_url)
api = Api(
    blueprint,
    title="API v1.0",
    version="1.0",
    description="A description",
    authorizations={"Bearer Auth": {"type": "apiKey", "in": "header", "name": "Authorization"}},
    security="Bearer Auth",
    doc=doc,
)


apidoc.Apidoc.static_url_path = base_url + "/swaggerui"


@api.documentation
def custom_ui():
    return apidoc.ui_for(api)


@api.errorhandler(JWTExtendedException)
def handle_jwt_exceptions(error):
    return response.bad(str(error))


api.add_namespace(user)

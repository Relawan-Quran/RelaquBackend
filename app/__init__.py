from flask import Flask
from flask_jwt_extended import JWTManager
from app.mod_api_v1 import blueprint as mod_api_v1, response, api
from app.mod_dashboard_v1 import blueprint as mod_dashboard_v1

app = Flask(__name__, static_url_path='/static')
app.config.from_object("config")

jwt = JWTManager(app)


@jwt.unauthorized_loader
def jwt_unauthorized_callback(self):
    return response.bad("Unathorized Token", 401)


@jwt.expired_token_loader
def my_expired_token_callback(jwt_header, jwt_payload):
    return response.bad("Expired Token", 401)


@jwt.invalid_token_loader
def my_invalid_token_callback(jwt_header):
    return response.bad("Invalid Token", 401)


jwt._set_error_handler_callbacks(api)

# Register blueprint(s)
app.register_blueprint(mod_api_v1)
app.register_blueprint(mod_dashboard_v1)

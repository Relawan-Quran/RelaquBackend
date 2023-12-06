from flask_restx import fields, Namespace

ns_user = Namespace("user", "Namespace User")

LoginSchema = ns_user.model(
    "LoginSchema",
    {
        "username": fields.String(description="Username", required=True),
        "password": fields.String(description="Password", required=True),
    },
)

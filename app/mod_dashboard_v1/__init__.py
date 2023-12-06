from flask import Blueprint, request
blueprint = Blueprint("dashboard_v1", __name__, url_prefix="/")

import app.mod_dashboard_v1.user # noqa
import app.mod_dashboard_v1.home # noqa
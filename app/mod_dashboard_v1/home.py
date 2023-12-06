from app.mod_dashboard_v1 import blueprint as bp
from flask import render_template, request, \
                  flash, g, session, redirect, url_for


@bp.route("/", methods=("GET", "POST"))
def index():
    data = {
        "name": "RelaQu"
    }
    return render_template("home/index.html", data=data)

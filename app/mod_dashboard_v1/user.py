from app.mod_dashboard_v1 import blueprint as bp
from flask import render_template, request, \
                  flash, g, session, redirect, url_for


@bp.route('/user', methods=('GET', 'POST'))
def user_index():
    return render_template("user/index.html")


@bp.route('/user/login', methods=('GET', 'POST'))
def login():
    return render_template("user/login.html")


@bp.route('/user/register', methods=('GET', 'POST'))
def register():
    return render_template("user/register.html")

# https://github.com/perogeremmer/flask-todo-list/blob/master/app/response.py


def ok(data, message):
    res = {"success": True, "message": message, "data": data}

    return res, 200


def bad(message, code=501):
    res = {"success": False, "message": message}

    return res, code

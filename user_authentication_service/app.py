#!/usr/bin/env python3
"""Script contains flask app"""
from flask import Flask, jsonify, request, make_response, abort, flask
from sqlalchemy.orm.exc import NoResultFound
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route("/")
def payload():
    """Function returns payload"""
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=['POST'])
def users():
    """Function registers new user to db"""
    email = request.form.get("email")
    password = request.form.get("password")

    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": f"{user.email}", "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"})


@app.route("/sessions", methods=['POST'])
def login():
    """Function creates, session_id, logs in, returns cookies"""
    email = request.form.get("email")
    password = request.form.get("password")
    is_valid = AUTH.valid_login(email, password)
    if is_valid:
        session_id = AUTH.create_session(email)

        response = make_response(
            jsonify({"email": f"{email}", "message": "logged in"}))
        response.set_cookie("session_id", session_id)

        return response
    else:
        abort(401)


@app.route("/sessions", methods=['DELETE'])
def logout():
    """Function finds user by session_id and then kills session"""
    try:
        session_id = request.cookies.get("session_id")
        user = AUTH.get_user_from_session_id(session_id)
        AUTH.destroy_session(user.id)
        return redirect("/")
    except NoResultFound:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)

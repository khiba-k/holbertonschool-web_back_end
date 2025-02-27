#!/usr/bin/env python3
"""Script contains flask app"""
from flask import Flask, jsonify, request, make_response, abort
from sqlalchemy.orm.exc import NoResultFound
from auth import Auth


Auth = Auth()
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
        user = Auth.register_user(email, password)
        return jsonify({"email": f"{user.email}", "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"})


@app.route("/sessions", methods=['POST'])
def login():
    """Function creates, session_id, logs in, returns cookies"""
    email = request.form.get("email")
    password = request.form.get("password")
    is_valid = Auth.valid_login(email, password)
    if is_valid:
        session_id = Auth.create_session(email)

        response = make_response(
            jsonify({"email": f"{email}", "message": "logged in"}))
        response.set_cookie("session_id", session_id)

        return response
    else:
        abort(401)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)

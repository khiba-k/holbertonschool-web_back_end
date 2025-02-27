#!/usr/bin/env python3
"""Script contains flask app"""
from flask import Flask, jsonify, request
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)

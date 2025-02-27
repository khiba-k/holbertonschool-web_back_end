#!/usr/bin/env python3
"""Script contains flask app"""
from flask import Flask, jsonify


app = Flask(__name__)


@app.route("/")
def payload():
    """Function returns payload"""
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

#!/usr/bin/env python3
""" Basic flask app"""

from flask import Flask, jsonify, request
from auth import Auth

AUTH = Auth()
app = Flask(__name__)

app.url_map.strict_slashes = False


@app.route('/')
def hello_world():
    """ hello world """
    return jsonify({"message": "Bienvenue"})

@app.route('/users', methods=['POST'])
def register_user():
    """ Register a user """
    email = request.form.get("email")
    password = request.form.get("password")
    user = AUTH.register_user(email, password)
    return jsonify({"email": user.email, "message": "user created"})

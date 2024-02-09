#!/usr/bin/env python3
""" Basic flask app"""

from flask import Flask, jsonify, request, abort, make_response
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


@app.route('/sessions', methods=['POST'])
def login():
    """ Log in """
    email = request.form.get("email")
    password = request.form.get("password")
    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        if session_id:
            response = make_response(
                jsonify({"email": email,
                         "session_id": session_id,
                         "message": "logged in"}))
            response.set_cookie('session_id', session_id)
            return response
    abort(401)

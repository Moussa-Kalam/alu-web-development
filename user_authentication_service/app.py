#!/usr/bin/env python3
""" Basic flask app"""

from flask import Flask, jsonify
from auth import Auth

AUTH = Auth()
app = Flask(__name__)

app.url_map.strict_slashes = False


@app.route('/')
def hello_world():
    """hello world"""
    return jsonify({"message": "Bienvenue"})

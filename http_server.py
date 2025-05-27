from os import stat
from flask import Flask, jsonify
from markupsafe import escape

app = Flask(__name__)


@app.route("/salam")
def salam_handler():
    return "Eleyke"


@app.route("/api/data")
def api_data_handler():
    static_data = {"name": "Toybox", "amount": "2k", "unit": "kg"}

    return jsonify(static_data)

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'
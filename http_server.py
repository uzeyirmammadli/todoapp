from os import stat
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/salam")
def salam_handler():
    return "Eleyke"


@app.route("/api/data")
def api_data_handler():
    static_data = {"name": "Toybox", "amount": "2k", "unit": "kg"}

    return jsonify(static_data)

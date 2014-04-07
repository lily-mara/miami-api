#!/usr/bin/env python3
from flask import Flask, jsonify
import miami_api

app = Flask(__name__)

@app.route('/miami/open', methods = ['GET'])
def get_open():
	return jsonify(miami_api.get_open())

@app.route('/miami/hours/<string:location>', methods = ['GET'])
def get_hours(location):
	return jsonify(miami_api.get_hours(location))

@app.route('/miami/today', methods = ['GET'])
def get_today_hours():
	return jsonify(miami_api.get_today_hours())

if __name__ == '__main__':
    app.run(debug = True)

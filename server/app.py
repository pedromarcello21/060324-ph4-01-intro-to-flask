#!/usr/bin/env python3

from flask import make_response, jsonify
from config import app

@app.get('/')
def index():
    return make_response( "<h1>Hello World</h1>" )

@app.get('/greeting')
def greeting():
    greet = {"response": "Hello!"}
    return greet

@app.get('/count-to/<int:x>')
def count(x):
    list = []
    for i in range(x):
        list.append(i+1)
    return list

@app.get('/lower-case/<string:incoming_string>')
def lower_case(incoming_string):
    return {"result":incoming_string.lower()}

# write your routes here!

if __name__ == '__main__':
    app.run(port=5555, debug=True)

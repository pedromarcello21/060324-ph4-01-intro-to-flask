#!/usr/bin/env python3

from flask import Flask, make_response, jsonify

app = Flask(__name__)
app.json.compact = False

@app.get('/')
def index():
    return make_response( "<h1>Hello World</h1>" )

@app.get('/store')
def store():
    return { "hamburger": { "price": 12.00} }

@app.get('/other-site')
def stuff():
    return "<a href='http://www.reddit.com'>Go to reddit</a>"

@app.get('/blog/<string:name>')
def show_blog(name:str):
    return f"{name} has an amazing blog check it out"

@app.get('/math/<int:number_one>/<int:number_two>')
def add(number_one, number_two):
    return make_response( jsonify( {"result": number_one + number_two} ) )

# @app.get('/raccoons/<int:id>')

# write your routes here!

if __name__ == '__main__':
    app.run(port=5555, debug=True)

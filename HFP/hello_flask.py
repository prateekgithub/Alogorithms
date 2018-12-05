#!/usr/bin/env python3
from flask import Flask
from vsearch import search4letters

app = Flask(__name__)

@app.route('/')
def hello() -> str:
    return 'Hello world from flask'

@app.route('/search4')
def do_search() -> set:
    return search4letters(“life, the universe, and everything”, 'eiru,!')

app.run()
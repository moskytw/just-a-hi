#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request, render_template

app = Flask(__name__)
# the error dump will be printed to uwsgi's error long
app.debug = True

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.route('/')
def index():
    return about()

@app.route('/about')
def about():
    return render_template('about.html')

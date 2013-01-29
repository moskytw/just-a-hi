#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request, render_template

app = Flask(__name__)
# the error dump will be printed to uwsgi's error long
app.debug = True

@app.route('/')
def index():
    return about()

@app.route('/about')
def about():
    return render_template('about.html')

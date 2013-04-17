#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request, render_template
import yaml

app = Flask(__name__)

with open('flask/app.yaml') as f:
    app.config.update(yaml.load(f))

with open('flask/secret-key.yaml') as f:
    app.config.update(yaml.load(f))

import logging
from logging import Formatter, FileHandler

file_handler = FileHandler('log/app.log')
app.logger.addHandler(file_handler)
file_handler.setFormatter(Formatter(
    '%(asctime)s %(levelname)s %(pathname)s:%(lineno)d %(message)s'
))

if app.debug:
    file_handler.setLevel(logging.DEBUG)
else:
    file_handler.setLevel(logging.WARNING)

@app.errorhandler(404)
@app.route('/404')
def not_found(error=None):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(error):

    from datetime import datetime

    other = {
        'occursed_at': datetime.now(),
    }

    from sys import exc_info
    from traceback import format_exception

    if app.debug:
        return render_template(
            '500.html',
            traceback = format_exception(*exc_info()),
            other     = other
        ), 500
    else:
        from . import mail
        app.logger.error('sent a mail for 500, return: %r' % mail.send(app.config['ADMIN_EMAILS'], '500 Internal Server Error', render_template(
            'mail_500.md',
            traceback = format_exception(*exc_info()),
            other     = other
        )))
        return render_template('500.html'), 500

@app.route('/')
def index():
    return about()

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/test_500')
def make_error():
    raise Exception('A fake exception')

@app.route('/test_log/<msg>')
def log(msg):
    app.logger.debug(msg)
    return msg

@app.route('/person/')
def person():
    from .model import Person
    return str(list(Person.seek(request.args)))

@app.route('/unsafe_person/')
def unsafe_person():
    from .model import Person
    sql_tmpl = "select * from person where person_id='%s'"
    return str(Person.run(sql_tmpl % request.args.get('person_id')).fetchall())

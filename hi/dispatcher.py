#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request, render_template
import yaml

app = Flask(__name__)

with open('config.yaml') as f:
    app.config.update(yaml.load(f))

with open('secret-key.yaml') as f:
    app.config.update(yaml.load(f))

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(error):

    from datetime import datetime

    saved_path = None
    occursed_at = datetime.now()

    if not app.debug:
        from os.path import dirname, join
        saved_path = join(
            dirname(__file__),
            'errors',
            '%s-%s-%s-%s.html' % (
                occursed_at.isoformat(),
                type(error).__name__.lower(),
                error.message,
                request.environ['REMOTE_ADDR'])
        )

    other = {
        'occursed_at': occursed_at,
        'saved_path' : saved_path,
    }

    from sys import exc_info
    from traceback import format_exception

    dumped_text = render_template(
            '500.html',
        traceback = format_exception(*exc_info()),
        request_  = request,
        other     = other
    )

    if saved_path:
        # TODO: the error viewer, and send a mail here
        with open(saved_path, 'w') as f:
            f.write(dumped_text)
        return render_template('500.html'), 500
    else:
        return dumped_text, 500

@app.route('/test500')
def make_error():
    raise Exception('A fake exception')

@app.route('/')
def index():
    return about()

@app.route('/about')
def about():
    return render_template('about.html')

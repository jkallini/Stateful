#!/usr/bin/env python

# -----------------------------------------------------------------------
# error.py
# author: Julie Kallini
# -----------------------------------------------------------------------

from flask import Flask, Blueprint, render_template


page = Blueprint('error', __name__)


# 404 error message
@page.app_errorhandler(404)
def page_not_found(e):
    return render_template('message.html',
                           title='Oops!',
                           message='The page you are looking for ' +
                           'does not exist.<br> ' +
                           'Click <a href="/">here</a> to ' +
                           'return to the home page.'), 404


@page.app_errorhandler(500)
def server_error(e):
    return render_template('message.html',
                           title='A server error occurred.',
                           message="Please try again later."), 500


@page.app_errorhandler(405)
def bad_method(e):
    return render_template('message.html',
                           title='Bad method',
                           message="This request method has been disabled."), 405
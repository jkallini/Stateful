#!/usr/bin/env python

#-----------------------------------------------------------------------
# app.py
# author: Julie Kallini
#-----------------------------------------------------------------------

from flask import Flask, render_template, url_for, request, make_response
import fsm as FSM

app = Flask(__name__)


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    html = render_template('index.html')
    response = make_response(html)
    return response


@app.route('/editor')
def editor():
    return render_template('editor.html')


@app.route('/problem/<int:probid>')
def problem(probid):
    return render_template('problem.html')


@app.route('/fsmreceiver', methods=['POST'])
def fsmreceiver():
    fsm_json = request.form['fsm_json']
    deterministic = request.form['deterministic']
    if deterministic == 'true':
        det = True
    else:
        det = False
    return FSM.parse_json(fsm_json, det)

if __name__ == "__main__":
    app.run(debug=True)

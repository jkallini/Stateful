#!/usr/bin/env python

# -----------------------------------------------------------------------
# app.py
# author: Julie Kallini
# -----------------------------------------------------------------------

from flask import Flask, render_template, url_for, request, make_response
import translator as TL
import fsm as FSM
import json

app = Flask(__name__)


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    html = render_template('index.html')
    return make_response(html)


@app.route('/editor')
def editor():
    return render_template('editor.html')


@app.route('/problem/<int:probid>')
def problem(probid):

    if not TL.probid_exists(probid):
        # TODO: do real error handling here
        return render_template('index.html')

    html = render_template('problem.html',
    probid=probid,
    description=TL.get_problem_description(probid))
    response = make_response(html)
    return response


@app.route('/submit', methods=['POST'])
def submit():

    # get JS variables
    fsm_json = request.form['fsm_json']
    deterministic = request.form['deterministic']

    # set boolean if deterministic is true
    if deterministic == 'true':
        det = True
    else:
        det = False

    error, fsm_or_exception = FSM.parse_json(fsm_json, det)

    if error:
        response = {'title': "Oops!",
                    'message': str(fsm_or_exception)}
        return json.dumps(response)
    else:
        response = {'title': "Good Job!",
                    'message': FSM.fsm_str(fsm_or_exception)}
        return json.dumps(response)


if __name__ == "__main__":
    app.run(debug=True)

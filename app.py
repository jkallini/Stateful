#!/usr/bin/env python

# -----------------------------------------------------------------------
# app.py
# author: Julie Kallini
# -----------------------------------------------------------------------

from flask import Flask, render_template, url_for, request, make_response
import translator as TL
import fsm as FSM
from problem import Problem
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

    problem = TL.get_problem(probid)
    html = render_template('problem.html',
    probid=probid,
    description=problem.get_description())
    response = make_response(html)
    return response


@app.route('/submit', methods=['POST'])
def submit():

    # get JS variables
    fsm_json = request.form['fsm_json']
    probid = int(request.form['probid'])

    if not TL.probid_exists(probid):
        response = {'title': "An Error Occurred",
                    'message': "Sorry for the inconvenience!"}
        return response

    problem = TL.get_problem(probid)

    det = problem.is_deterministic()

    error, fsm_or_exception = FSM.parse_json(fsm_json, det)

    if error:
        response = {'title': "Oops!",
                    'message': str(fsm_or_exception)}
        return json.dumps(response)

    solution = problem.get_fsm()

    if not FSM.equal(solution, fsm_or_exception):
        response = {'title': "Incorrect",
        'message': "That's not quite right. Give it another try!"}
    else:
        response = {'title': "Good Job!",
                    'message': FSM.fsm_str(fsm_or_exception)}
    return json.dumps(response)


if __name__ == "__main__":
    app.run(debug=True)

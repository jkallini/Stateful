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


# error handling page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    html = render_template('index.html')
    response = make_response(html)
    return response


@app.route('/lesson/<string:lessonid>')
def lesson(lessonid):
    if lessonid == '1.1':
        html = render_template('lessons/lesson1-1.html')
    elif lessonid == '1.2':
        html = render_template('lessons/lesson1-2.html')
    elif lessonid == '1.3':
        html = render_template('lessons/lesson1-3.html')
    elif lessonid == '2.1':
        html = render_template('lessons/lesson2-1.html')
    elif lessonid == '2.2':
        html = render_template('lessons/lesson2-2.html')
    elif lessonid == '2.3':
        html = render_template('lessons/lesson2-3.html')
    else:
        html = render_template('index.html')

    return make_response(html)


@app.route('/DFApractice')
def DFApractice():
    DFA_probs = TL.get_DFA_problems()
    html = render_template(
        'practice.html', probs=DFA_probs, det=True)
    response = make_response(html)
    return response

@app.route('/NFApractice')
def NFApractice():
    NFA_probs = TL.get_NFA_problems()
    html = render_template(
        'practice.html', probs=NFA_probs, det=False)
    response = make_response(html)
    return response

@app.route('/DFAproblem/<int:probid>')
def DFA_problem(probid):

    if not TL.DFA_probid_exists(probid):
        # TODO: do real error handling here
        return render_template('index.html')

    problem = TL.get_DFA_problem(probid)
    html = render_template('problem.html', problem=problem)
    response = make_response(html)
    return response


@app.route('/NFAproblem/<int:probid>')
def NFA_problem(probid):

    if not TL.NFA_probid_exists(probid):
        # TODO: do real error handling here
        return render_template('index.html')

    problem = TL.get_NFA_problem(probid)
    html = render_template('problem.html', problem=problem)
    response = make_response(html)
    return response


@app.route('/submit', methods=['POST'])
def submit():

    # get JS variables
    fsm_json = request.form['fsm_json']
    probid = int(request.form['probid'])
    det = (request.form['deterministic'] == 'True')

    # get the problem and parse it into JSON
    if det:
        # verify that this problem exists (it should)
        if not TL.DFA_probid_exists(probid):
            response = {'title': "An Error Occurred",
                'message': "Sorry for the inconvenience!"}
            return response

        problem = TL.get_DFA_problem(probid)
    else:
        # verify that this problem exists (it should)
        if not TL.NFA_probid_exists(probid):
            response = {'title': "An Error Occurred",
                'message': "Sorry for the inconvenience!"}
            return response
        problem = TL.get_NFA_problem(probid)
    error, fsm_or_exception = FSM.parse_json(fsm_json, det)

    # check if the input is valid
    if error:
        response = {'title': "Oops! Your FSM is invalid!",
                    'message': str(fsm_or_exception)}
        return json.dumps(response)

    # retrieve solution
    solution = problem.get_fsm()
    exact = problem.is_exact()

    # check student's answer against solution
    if not FSM.equal(solution, fsm_or_exception, exact):
        response = {'title': "Incorrect",
                    'message': "That's not quite right. Give it another try!"}
    else:
        response = {'title': "Good Job!",
                    'message': 'Here is the 5-tuple for your FSM: <br>'
                    + FSM.fsm_str(fsm_or_exception)}
    return json.dumps(response)


if __name__ == "__main__":
    app.run(port=5555, debug=True)

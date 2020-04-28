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


# 404 error message
@app.errorhandler(404)
def page_not_found(e):
    return render_template('message.html',
                           title='Oops!',
                           message='The page you are looking for ' +
                           'does not exist.<br> ' +
                           'Click <a href="/">here</a> to ' +
                           'return to the home page.'), 404


@app.errorhandler(500)
def server_error(e):
    return render_template('message.html',
                           title='A server error occurred.',
                           message="Please try again later."), 500


@app.errorhandler(405)
def bad_method(e):
    return render_template('message.html',
                           title='Bad method',
                           message="This request method has been disabled."), 405


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
        return render_template('message.html',
                               title='Oops!',
                               message='The lesson you are looking for ' +
                               'does not exist.<br> ' +
                               'Click <a href="/">here</a> to ' +
                               'return to the home page.'), 404

    return make_response(html)


@app.route('/tutorial')
def tutorial():
    html = render_template('tutorial.html')
    response = make_response(html)
    return response


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
        return render_template('message.html',
                               title='Oops!',
                               message='The DFA problem you are looking for ' +
                               'does not exist.<br> ' +
                               'Click <a href="/DFApractice">here</a> to ' +
                               'view other DFA problems.'), 404

    problem = TL.get_DFA_problem(probid)
    html = render_template('problem.html', problem=problem)
    response = make_response(html)
    return response


@app.route('/NFAproblem/<int:probid>')
def NFA_problem(probid):

    if not TL.NFA_probid_exists(probid):
        return render_template('message.html',
                               title='Oops!',
                               message='The NFA problem you are looking for ' +
                               'does not exist.<br> ' +
                               'Click <a href="/NFApractice">here</a> to ' +
                               'view other NFA problems.'), 404

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
        response = {'title': "Great Job!",
                    'message': 'Here is the 5-tuple for your FSM: <br>'
                    + FSM.fsm_str(fsm_or_exception)}
    return json.dumps(response)


if __name__ == "__main__":
    app.run(port=5555, debug=True)

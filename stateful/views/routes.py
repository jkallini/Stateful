#!/usr/bin/env python

# -----------------------------------------------------------------------
# app.py
# author: Julie Kallini
# -----------------------------------------------------------------------

from flask import Blueprint, render_template, url_for, request, \
    make_response
from stateful.models.problem import Problem
import stateful.models.bank as Bank
import stateful.models.fsm as FSM
import json


page = Blueprint('routes', __name__)


@page.route('/', methods=['GET'])
@page.route('/index', methods=['GET'])
def index():
    html = render_template('index.html')
    response = make_response(html)
    return response


@page.route('/lesson/<string:lessonid>')
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


@page.route('/tutorial')
def tutorial():
    html = render_template('tutorial.html')
    response = make_response(html)
    return response


@page.route('/citations')
def citations():
    html = render_template('citations.html')
    response = make_response(html)
    return response


@page.route('/DFApractice')
def DFApractice():
    DFA_probs = Bank.get_DFA_problems()
    html = render_template(
        'practice.html', probs=DFA_probs, det=True)
    response = make_response(html)
    return response


@page.route('/NFApractice')
def NFApractice():
    NFA_probs = Bank.get_NFA_problems()
    html = render_template(
        'practice.html', probs=NFA_probs, det=False)
    response = make_response(html)
    return response


@page.route('/DFAproblem/<int:probid>')
def DFA_problem(probid):

    if not Bank.DFA_probid_exists(probid):
        return render_template('message.html',
                               title='Oops!',
                               message='The DFA problem you are looking for ' +
                               'does not exist.<br> ' +
                               'Click <a href="/DFApractice">here</a> to ' +
                               'view other DFA problems.'), 404

    problem = Bank.get_DFA_problem(probid)
    html = render_template('problem.html', problem=problem)
    response = make_response(html)
    return response


@page.route('/NFAproblem/<int:probid>')
def NFA_problem(probid):

    if not Bank.NFA_probid_exists(probid):
        return render_template('message.html',
                               title='Oops!',
                               message='The NFA problem you are looking for ' +
                               'does not exist.<br> ' +
                               'Click <a href="/NFApractice">here</a> to ' +
                               'view other NFA problems.'), 404

    problem = Bank.get_NFA_problem(probid)
    html = render_template('problem.html', problem=problem)
    response = make_response(html)
    return response


@page.route('/submit', methods=['POST'])
def submit():

    # get JS variables
    fsm_json = request.form['fsm_json']
    probid = int(request.form['probid'])
    det = (request.form['deterministic'] == 'True')
    
    return get_feedback(fsm_json, probid, det)


def get_feedback(fsm_json, probid, det):
    
    # get the problem and parse it into JSON
    if det:
        # verify that this problem exists (it should)
        if not Bank.DFA_probid_exists(probid):
            response = {'title': "An Error Occurred",
                        'message': "Sorry for the inconvenience!"}
            return response

        problem = Bank.get_DFA_problem(probid)
    else:
        # verify that this problem exists (it should)
        if not Bank.NFA_probid_exists(probid):
            response = {'title': "An Error Occurred",
                        'message': "Sorry for the inconvenience!"}
            return response
        problem = Bank.get_NFA_problem(probid)
    error, fsm_or_exception = FSM.parse_json(fsm_json, det)

    # check if the input is valid
    if error:
        response = {'title': "Oops! Your FSM is invalid!",
                    'message': str(fsm_or_exception)}
        return json.dumps(response)

    # retrieve solution
    solution = problem.get_fsm()
    exact = problem.is_exact()

    # check alphabet
    if not FSM.valid_alphabet(solution, fsm_or_exception, det):
        response = {'title': "Incorrect",
                    'message': "That's not quite right. Give it another try!",
                    'hint': "Check the alphabet of your FSM. Is it " + \
                        "missing any symbols? Does it have any extraneous symbols?"}
        return json.dumps(response)

    # check student's answer against solution
    equal = FSM.equal(solution, fsm_or_exception, exact)

    # if question requires exact match, generate simple hint
    if (not equal) and exact:
        response = {'title': "Incorrect",
                'message': "That's not quite right. Give it another try!",
                'hint': "Did you label all states and transitions correctly?" + \
                    " Are the appropriate accept states indicated?"}
        return json.dumps(response)

    # make alphabets equal, in case this was an issue
    fsm_or_exception.input_symbols = solution.input_symbols
    if not equal:
        assert(FSM.equal_alphabets(fsm_or_exception, solution))
        response = {'title': "Incorrect",
                    'message': "That's not quite right. Give it another try!",
                    'solution_fsm': FSM.noam_fsm(FSM.determinize(solution)),
                    'student_fsm': FSM.noam_fsm(FSM.determinize(fsm_or_exception))}
    else:
        response = {'title': "Great Job!",
                    'message': 'Here is the 5-tuple for your FSM: <br>'
                    + FSM.fsm_str(fsm_or_exception)}
    return json.dumps(response)

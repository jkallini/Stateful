#!/usr/bin/env python

# -----------------------------------------------------------------------
# translator.py
# author: Julie Kallini
# -----------------------------------------------------------------------

import fsm as FSM
from problem import Problem
from automata.fa.dfa import DFA
from automata.fa.nfa import NFA

problem_bank = {
    1: Problem(probid=1,
               description="Design a DFA that accepts all strings of a\'s or b\'s.",
               fsm=DFA(states={'1'},
                       input_symbols={'b', 'a'},
                       transitions={'1': {'a': '1', 'b': '1'}},
                       initial_state='1',
                       final_states={'1'})
               )
}


def probid_exists(probid):
    return (probid in problem_bank)


def get_problem_description(probid):
    return problem_bank[probid].get_description()

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
               description="Design a DFA that recognizes \(L = \{ a,b\}^*\), the language of all strings that contain \(a\)\'s or \(b\)\'s.",
               fsm=DFA(states={'1'},
                       input_symbols={'a', 'b'},
                       transitions={'1': {'a': '1', 'b': '1'}},
                       initial_state='1',
                       final_states={'1'})
               ),
    2: Problem(probid=2,
               description="Design a DFA that recognizes the language \(L \in \{ a,b\}^*\), <br/> where the number of \(b\)'s is even.",
               fsm=DFA(states={'1', '2'},
                       input_symbols={'a', 'b'},
                       transitions={'1': {'a': '1', 'b': '2'}, '2': {'b': '1', 'a': '2'}},
                       initial_state='1',
                       final_states={'1'})
               ),
}


def probid_exists(probid):
    return (probid in problem_bank)


def get_problem(probid):
    if not probid_exists(probid):
        return "probid " + str(probid) + " does not exist"
    return problem_bank[probid]

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

    # DFA problems
    1: Problem(probid=1,
               description="Design a DFA that recognizes \(\color{#056fa0}{L = \{ a,b\}^*}\), <br/> the language of all strings that contain \(\color{#056fa0}{a}\)\'s or \(\color{#056fa0}{b}\)\'s.",
               fsm=DFA(states={'1'},
                       input_symbols={'a', 'b'},
                       transitions={'1': {'a': '1', 'b': '1'}},
                       initial_state='1',
                       final_states={'1'})
               ),
    2: Problem(probid=2,
               description="Design a DFA that recognizes the language \(\color{#056fa0}{L \subseteq \{ a,b\}^*}\), <br/> where the number of \(\color{#056fa0}{b}\)'s is even.",
               fsm=DFA(states={'1', '2'},
                       input_symbols={'a', 'b'},
                       transitions={'1': {'a': '1', 'b': '2'},
                                    '2': {'b': '1', 'a': '2'}},
                       initial_state='1',
                       final_states={'1'})
               ),
    3: Problem(probid=3,
               description="Design a DFA that recognizes the language \(\color{#056fa0}{L \subseteq \{ x, y\}^*}\) <br> of strings that begin with \(\color{#056fa0}{x}\) and end with \(\color{#056fa0}{y}\).",
               fsm=DFA(states={'1', '2', '3', '4'},
                       input_symbols={'x', 'y'},
                       transitions={'1': {'y': '2', 'x': '3'},
                                    '2': {'y': '2', 'x': '2'},
                                    '3': {'y': '4', 'x': '3'},
                                    '4': {'y': '4', 'x': '3'}},
                       initial_state='1',
                       final_states={'4'})
               ),
    4: Problem(probid=4,
               description="Design a DFA that recognizes the language \( \color{#056fa0}{ L = \{ w \in \{0\}^* : |w| \\text{ is not divisible by } 3 \} } \).",
               fsm=DFA(states={'1', '2', '3'},
                       input_symbols={'0'},
                       transitions={'1': {'0': '2'},
                                    '2': {'0': '3'},
                                    '3': {'0': '1'}},
                       initial_state='1',
                       final_states={'2', '3'})
               ),
    5: Problem(probid=5,
               description="Design an NFA that recognizes the strings 'cat' and 'cats' only. <br> You may assume that the input alphabet is \(\color{#056fa0}{\Sigma = \{ c, a, t, s\}}\).",
               fsm=NFA(states={'1', '2', '3', '4', '5'},
                       input_symbols={'c', 'a', 't', 's', ''},
                       transitions={'1': {'c': {'2'}}, '2': {'a': {'3'}}, '3': {
                           't': {'4'}}, '4': {'s': {'5'}}, '5': {}},
                       initial_state='1',
                       final_states={'4', '5'})
               )
}


def probid_exists(probid):
    return (probid in problem_bank)


def get_problem(probid):
    if not probid_exists(probid):
        return "probid " + str(probid) + " does not exist"
    return problem_bank[probid]

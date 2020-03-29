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
               description="Design a DFA that recognizes \(\color{#056fa0}{L = \{ a,b\}^*}\), <br/> the language of all strings with any number of \(\color{#056fa0}{a}\)\'s or \(\color{#056fa0}{b}\)\'s.",
               fsm=DFA(states={'1'},
                       input_symbols={'a', 'b'},
                       transitions={'1': {'a': '1', 'b': '1'}},
                       initial_state='1',
                       final_states={'1'}),
               difficulty=Problem.EASY),
    2: Problem(probid=2,
               description="Design a DFA that recognizes the language \(\color{#056fa0}{L \subseteq \{ a,b\}^*}\), <br/> where the number of \(\color{#056fa0}{b}\)'s is even.",
               fsm=DFA(states={'1', '2'},
                       input_symbols={'a', 'b'},
                       transitions={'1': {'a': '1', 'b': '2'},
                                    '2': {'b': '1', 'a': '2'}},
                       initial_state='1',
                       final_states={'1'}),
               difficulty=Problem.EASY
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
                       final_states={'4'}),
               difficulty=Problem.EASY
               ),
    4: Problem(probid=4,
               description="Design a DFA over the alphabet \(\color{#056fa0}{\Sigma = \{a,b,c\}}\) that accepts any string with \(\color{#056fa0}{aab}\) as a substring.",
               fsm=DFA(states={'1', '2', '3', '4'},
                       input_symbols={'a', 'b', 'c'},
                       transitions={'1': {'a': '2', 'b': '1', 'c': '1'},
                                    '2': {'a': '3', 'b': '1', 'c': '1'},
                                    '3': {'a': '3', 'b': '4', 'c': '1'},
                                    '4': {'a': '4', 'b': '4', 'c': '4'}},
                       initial_state='1',
                       final_states={'4'}),
               difficulty=Problem.MEDI
               ),
    5: Problem(probid=5,
               description="Design a DFA that recognizes the language \( \color{#056fa0}{ L = \{ w \in \{0\}^* : |w| \\text{ is not divisible by } 3 \} } \).",
               fsm=DFA(states={'1', '2', '3'},
                       input_symbols={'0'},
                       transitions={'1': {'0': '2'},
                                    '2': {'0': '3'},
                                    '3': {'0': '1'}},
                       initial_state='1',
                       final_states={'2', '3'}),
               difficulty=Problem.MEDI
               ),
    6: Problem(probid=6,
               description="Design an NFA that recognizes the strings 'cat' and 'cats' only. <br> You may assume that the input alphabet is \(\color{#056fa0}{\Sigma = \{ c, a, t, s\}}\).",
               fsm=NFA(states={'1', '2', '3', '4', '5'},
                       input_symbols={'c', 'a', 't', 's', ''},
                       transitions={'1': {'c': {'2'}},
                                    '2': {'a': {'3'}},
                                    '3': {'t': {'4'}},
                                    '4': {'s': {'5'}},
                                    '5': {}},
                       initial_state='1',
                       final_states={'4', '5'}),
               difficulty=Problem.EASY
               ),
    7: Problem(probid=7,
               description="Design an NFA over the alphabet \(\color{#056fa0}{\Sigma = \{a,b,c\}}\) that accepts any string with \(\color{#056fa0}{aab}\) as a substring.",
               fsm=NFA(states={'1', '2', '3', '4'},
                       input_symbols={'a', 'b', 'c'},
                       transitions={'1': {'a': {'1', '2'}, 'b': {'1'}, 'c': {'1'}},
                                    '2': {'a': {'3'}, 'b': {'1'}, 'c': {'1'}},
                                    '3': {'a': {'3'}, 'b': {'4'}, 'c': {'1'}},
                                    '4': {'a': {'4'}, 'b': {'4'}, 'c': {'4'}}},
                       initial_state='1',
                       final_states={'4'}),
               difficulty=Problem.EASY
               ),
    8: Problem(probid=8,
               description="Design an NFA over the alphabet \(\color{#056fa0}{\Sigma = \{a,b,c\}}\) that accepts any string with \(\color{#056fa0}{ba}\) or \(\color{#056fa0}{cab}\) as a substring.",
               fsm=NFA(states={'1', '2', '3', '4', '5', '6', '7', '8'},
                       input_symbols={'a', 'b', 'c'},
                       transitions={'1': {'': {'2', '6'}},
                                    '2': {'c': {'3'}},
                                    '3': {'a': {'4'}},
                                    '4': {'b': {'5'}},
                                    '5': {},
                                    '6': {'b': {'7'}},
                                    '7': {'a': {'8'}},
                                    '8': {}},
                       initial_state='1',
                       final_states={'5', '8'}),
               difficulty=Problem.EASY
               )
}


def probid_exists(probid):
    return (probid in problem_bank)


def get_problem(probid):
    if not probid_exists(probid):
        return "probid " + str(probid) + " does not exist"
    return problem_bank[probid]

#!/usr/bin/env python

# -----------------------------------------------------------------------
# translator.py
# author: Julie Kallini
# -----------------------------------------------------------------------

import fsm as FSM
from problem import Problem
from automata.fa.dfa import DFA
from automata.fa.nfa import NFA


DFA_problem_bank = [
    Problem(probid=1,
            description="Design a DFA that recognizes \(\color{#056fa0}{L = \{ a,b\}^*}\), the language of all strings with any number of \(\color{#056fa0}{a}\)\'s or \(\color{#056fa0}{b}\)\'s.",
            fsm=DFA(states={'1'},
                    input_symbols={'a', 'b'},
                    transitions={'1': {'a': '1', 'b': '1'}},
                    initial_state='1',
                    final_states={'1'}),
            difficulty=Problem.EASY,
            exact=False),
    Problem(probid=2,
            description="Design a DFA that recognizes the language \(\color{#056fa0}{L \subseteq \{ a,b\}^*}\), where the number of \(\color{#056fa0}{b}\)'s is even.",
            fsm=DFA(states={'1', '2'},
                    input_symbols={'a', 'b'},
                    transitions={'1': {'a': '1', 'b': '2'},
                                 '2': {'b': '1', 'a': '2'}},
                    initial_state='1',
                    final_states={'1'}),
            difficulty=Problem.EASY,
            exact=False),
    Problem(probid=3,
            description="Design a DFA that recognizes the language \(\color{#056fa0}{L \subseteq \{ x, y\}^*}\) of strings that begin with \(\color{#056fa0}{x}\) and end with \(\color{#056fa0}{y}\).",
            fsm=DFA(states={'1', '2', '3', '4'},
                    input_symbols={'x', 'y'},
                    transitions={'1': {'y': '2', 'x': '3'},
                                 '2': {'y': '2', 'x': '2'},
                                 '3': {'y': '4', 'x': '3'},
                                 '4': {'y': '4', 'x': '3'}},
                    initial_state='1',
                    final_states={'4'}),
            difficulty=Problem.EASY,
            exact=False),
    Problem(probid=4,
            description="The formal description of a DFA \(\color{#056fa0}{M}\) is \(\color{#056fa0}{(\{s_0, s_1, s_2\}, \{0,1\}, \delta, s_0, \{s_0\})}\), where \(\color{#056fa0}{\delta}\) is given by the following table. Give the state diagram of this machine. (To give states labels with numberical subscripts, type 'q_0' etc.)"
            "<table style='text-align:center; margin-left:auto; margin-right:auto; font-size: 18px'>" +
            "<tr style='border-bottom: 1px solid black;'><td><span class='math-color'>\( \delta \)</span></td><td style='border-left: 1px solid black;'><span class='math-color'>\( 0 \)</span></td><td><span class='math-color'>\( 1 \)</span></td></tr><tr><td><span class='math-color'>\( s_0 \)</span></td><td style='border-left: 1px solid black;'><span class='math-color'>\( s_0 \)</span></td><td><span class='math-color'>\( s_1 \)</span></td></tr><tr><td><span class='math-color'>\( s_1 \)</span></td><td style='border-left: 1px solid black;'><span class='math-color'>\( s_0 \)</span></td><td><span class='math-color'>\( s_2 \)</span></td></tr><tr><td><span class='math-color'>\( s_2 \)</span></td><td style='border-left: 1px solid black;'><span class='math-color'>\( s_2 \)</span></td><td><span class='math-color'>\( s_1 \)</span></td></tr></table>",
            fsm=DFA(states={'s_0', 's_1', 's_2'},
                    input_symbols={'0', '1'},
                    transitions={'s_0': {'0': 's_0', '1': 's_1'},
                                 's_1': {'0': 's_0', '1': 's_2'},
                                 's_2': {'0': 's_2', '1': 's_1'}},
                    initial_state='s_0',
                    final_states={'s_0'}),
            difficulty=Problem.MEDI,
            exact=True),
    Problem(probid=5,
            description="Design a DFA over the alphabet \(\color{#056fa0}{\Sigma = \{a,b,c\}}\) that accepts any string with \(\color{#056fa0}{aab}\) as a substring.",
            fsm=DFA(states={'1', '2', '3', '4'},
                    input_symbols={'a', 'b', 'c'},
                    transitions={'1': {'a': '2', 'b': '1', 'c': '1'},
                                 '2': {'a': '3', 'b': '1', 'c': '1'},
                                 '3': {'a': '3', 'b': '4', 'c': '1'},
                                 '4': {'a': '4', 'b': '4', 'c': '4'}},
                    initial_state='1',
                    final_states={'4'}),
            difficulty=Problem.MEDI,
            exact=False),
    Problem(probid=6,
            description="Design a DFA that recognizes the language \( \color{#056fa0}{ L = \{ w \in \{0\}^* : |w| \\text{ is not divisible by } 3 \} } \).",
            fsm=DFA(states={'1', '2', '3'},
                    input_symbols={'0'},
                    transitions={'1': {'0': '2'},
                                 '2': {'0': '3'},
                                 '3': {'0': '1'}},
                    initial_state='1',
                    final_states={'2', '3'}),
            difficulty=Problem.MEDI,
            exact=False),
    Problem(probid=7,
            description="The formal description of a DFA \(\color{#056fa0}{M}\) is \(\color{#056fa0}{(\{q_1, q_2, q_3, q_4, q_5\}, \{u,d\}, \delta, q_3, \{q_3\})}\), where \(\color{#056fa0}{\delta}\) is given by the following table. Give the state diagram of this machine. (To give states labels with numberical subscripts, type 'q_0' etc.)" +
            "<table style='text-align:center; margin-left:auto; margin-right:auto; font-size: 18px'>" +
            "<tr style='border-bottom: 1px solid black;'><td><span class='math-color'>\( \delta \)</span></td><td style='border-left: 1px solid black;'><span class='math-color'>\( \\text{u} \)</span></td><td><span class='math-color'>\( \\text{d} \)</span></td></tr><tr><td><span class='math-color'>\( q_1 \)</span></td><td style='border-left: 1px solid black;'><span class='math-color'>\( q_1 \)</span></td><td><span class='math-color'>\( q_2 \)</span></td></tr><tr><td><span class='math-color'>\( q_2 \)</span></td><td style='border-left: 1px solid black;'><span class='math-color'>\( q_1 \)</span></td><td><span class='math-color'>\( q_3 \)</span></td></tr><tr><td><span class='math-color'>\( q_3 \)</span></td><td style='border-left: 1px solid black;'><span class='math-color'>\( q_2 \)</span></td><td><span class='math-color'>\( q_4 \)</span></td></tr><tr><td><span class='math-color'>\( q_4 \)</span></td><td style='border-left: 1px solid black;'><span class='math-color'>\( q_3 \)</span></td><td><span class='math-color'>\( q_5 \)</span></td></tr><tr><td><span class='math-color'>\( q_5 \)</span></td><td style='border-left: 1px solid black;'><span class='math-color'>\( q_5 \)</span></td><td><span class='math-color'>\( q_5 \)</span></td></tr></table>",
            fsm=DFA(states={'q_1', 'q_2', 'q_3', 'q_4', 'q_5'},
                    input_symbols={'u', 'd'},
                    transitions={'q_1': {'u': 'q_1', 'd': 'q_2'},
                                 'q_2': {'u': 'q_1', 'd': 'q_3'},
                                 'q_3': {'u': 'q_2', 'd': 'q_4'},
                                 'q_4': {'u': 'q_3', 'd': 'q_5'},
                                 'q_5': {'u': 'q_5', 'd': 'q_5'}},
                    initial_state='q_3',
                    final_states={'q_3'}),
            difficulty=Problem.HARD,
            exact=True),
    Problem(probid=8,
            description="Design a DFA that recognizes the language \(\color{#056fa0}{L = \{ w : w \\neq x1010y \\text{ where } x,y \in \{0,1\}^* \}}\).",
            fsm=DFA(states={'q_1', 'q_2', 'q_3', 'q_4', 'q_5'},
                    input_symbols={'0', '1'},
                    transitions={'q_1': {'0': 'q_1', '1': 'q_2'},
                                 'q_2': {'0': 'q_3', '1': 'q_2'},
                                 'q_3': {'0': 'q_1', '1': 'q_4'},
                                 'q_4': {'0': 'q_5', '1': 'q_2'},
                                 'q_5': {'0': 'q_5', '1': 'q_5'}},
                    initial_state='q_1',
                    final_states={'q_1', 'q_2', 'q_3', 'q_4'}),
            difficulty=Problem.HARD,
            exact=False),
    Problem(probid=9,
            description="Design a DFA that recognizes the language \(\color{#056fa0}{L = \{ w : w \\text{ starts with }a \\text{ and has odd length, or starts with }b \\text{ and has even length} \}}\).",
            fsm=DFA(states={'q_1', 'q_2', 'q_3', 'q_4', 'q_5'},
                    input_symbols={'a', 'b'},
                    transitions={'q_1': {'a': 'q_2', 'b': 'q_4'},
                                 'q_2': {'a': 'q_3', 'b': 'q_3'},
                                 'q_3': {'a': 'q_2', 'b': 'q_2'},
                                 'q_4': {'a': 'q_5', 'b': 'q_5'},
                                 'q_5': {'a': 'q_4', 'b': 'q_4'}},
                    initial_state='q_1',
                    final_states={'q_2', 'q_5'}),
            difficulty=Problem.HARD,
            exact=False)
]


NFA_problem_bank = [
    Problem(probid=1,
            description="Design an NFA that recognizes the language \(\color{#056fa0}{L = \{ 0, 1\}}\).",
            fsm=NFA(states={'1', '2', '3'},
                    input_symbols={'0', '1'},
                    transitions={'1': {'0': {'2'}, '1': {'3'}},
                                 '2': {},
                                 '3': {}},
                    initial_state='1',
                    final_states={'2', '3'}),
            difficulty=Problem.EASY,
            exact=False),
    Problem(probid=2,
            description="Design an NFA that recognizes the strings 'cat' and 'cats' only. You may assume that the input alphabet is \(\color{#056fa0}{\Sigma = \{ a,c,s,t\}}\).",
            fsm=NFA(states={'1', '2', '3', '4', '5'},
                        input_symbols={'c', 'a', 't', 's', ''},
                        transitions={'1': {'c': {'2'}},
                                     '2': {'a': {'3'}},
                                     '3': {'t': {'4'}},
                                     '4': {'s': {'5'}},
                                     '5': {}},
                        initial_state='1',
                        final_states={'4', '5'}),
            difficulty=Problem.EASY,
            exact=False),
    Problem(probid=3,
            description="Design an NFA over the alphabet \(\color{#056fa0}{\Sigma = \{a,b,c\}}\) that accepts any string with \(\color{#056fa0}{aab}\) as a substring.",
            fsm=NFA(states={'1', '2', '3', '4'},
                        input_symbols={'a', 'b', 'c', ''},
                        transitions={'1': {'a': {'1', '2'}, 'b': {'1'}, 'c': {'1'}},
                                     '2': {'a': {'3'}, 'b': {'1'}, 'c': {'1'}},
                                     '3': {'a': {'3'}, 'b': {'4'}, 'c': {'1'}},
                                     '4': {'a': {'4'}, 'b': {'4'}, 'c': {'4'}}},
                        initial_state='1',
                        final_states={'4'}),
            difficulty=Problem.EASY,
            exact=False),
    Problem(probid=4,
            description="The formal description of an NFA \(\color{#056fa0}{M}\) is \(\color{#056fa0}{(\{1, 2\}, \{a,b\}, \delta, 1, \{1\})}\), where \(\color{#056fa0}{\delta}\) is given by the following table. Give the state diagram of this machine."
            "<table style='text-align:center; margin-left:auto; margin-right:auto; font-size: 18px'>" +
                        "<tr style='border-bottom: 1px solid black;'><td><span class='math-color'>\( \delta \)</span></td><td style='border-left: 1px solid black;'><span class='math-color'>\( a \)</span></td><td><span class='math-color'>\( b \)</span></td></tr><tr><td><span class='math-color'>\( 1 \)</span></td><td style='border-left: 1px solid black;'><span class='math-color'>\( \{1,2\} \)</span></td><td><span class='math-color'>\( \{ 2 \} \)</span></td></tr><tr><td><span class='math-color'>\( 2 \)</span></td><td style='border-left: 1px solid black;'><span class='math-color'>\( \emptyset \)</span></td><td><span class='math-color'>\( \{ 1 \} \)</span></td></tr><tr></table>",
            fsm=NFA(states={'1', '2'},
                    input_symbols={'a', 'b'},
                    transitions={'1': {'a': {'1', '2'}, 'b': {'2'}},
                                 '2': {'b': {'1'}}},
                    initial_state='1',
                    final_states={'1'}),
            difficulty=Problem.EASY,
            exact=True),
    Problem(probid=5,
            description="Design an NFA that recognizes the language \(\color{#056fa0}{L = \{ w \in \{0,1\}^* : w = x0101y \\text{ for some } x,y \in \{ 1\}^* \}. }\)",
            fsm=NFA(states={'q1', 'q2', 'q3', 'q4', 'q5'},
                    input_symbols={'0', '1', ''},
                    transitions={'q1': {'0': {'q2'}, '1': {'q1'}},
                                 'q2': {'1': {'q3'}},
                                 'q3': {'0': {'q4'}},
                                 'q4': {'1': {'q5'}},
                                 'q5': {'1': {'q5'}}},
                    initial_state='q1',
                    final_states={'q5'}),
            difficulty=Problem.MEDI,
            exact=False),
    Problem(probid=6,
            description="Design an NFA over the alphabet \(\color{#056fa0}{\Sigma = \{a,b,c\}}\) that accepts any string with \(\color{#056fa0}{ba}\) or \(\color{#056fa0}{cab}\) as a substring.",
            fsm=NFA(states={'1', '2', '3', '4', '5', '6', '7', '8', '9'},
                        input_symbols={'a', 'b', 'c', ''},
                        transitions={'1': {'': {'2', '6'}, 'a': {'1'}, 'b': {'1'}, 'c': {'1'}},
                                     '2': {'c': {'3'}},
                                     '3': {'a': {'4'}},
                                     '4': {'b': {'5'}},
                                     '5': {'': {'9'}},
                                     '6': {'b': {'7'}},
                                     '7': {'a': {'8'}},
                                     '8': {'': {'9'}},
                                     '9': {'a': {'9'}, 'b': {'9'}, 'c': {'9'}}},
                        initial_state='1',
                        final_states={'9'}),
            difficulty=Problem.MEDI,
            exact=False)
]


def DFA_probid_exists(probid):
    return (probid <= len(DFA_problem_bank) and probid > 0)


def NFA_probid_exists(probid):
    return (probid <= len(NFA_problem_bank) and probid > 0)


def get_DFA_problem(probid):
    if not DFA_probid_exists(probid):
        return "DFA probid " + str(probid) + " does not exist"
    return DFA_problem_bank[probid-1]


def get_NFA_problem(probid):
    if not NFA_probid_exists(probid):
        return "NFA probid " + str(probid) + " does not exist"
    return NFA_problem_bank[probid-1]


def get_DFA_problems():
    DFA_problems = [(prob.get_id(), prob.get_description(), prob.get_difficulty())
                    for prob in DFA_problem_bank]
    return DFA_problems


def get_NFA_problems():
    NFA_problems = [(prob.get_id(), prob.get_description(), prob.get_difficulty())
                    for prob in NFA_problem_bank]
    return NFA_problems

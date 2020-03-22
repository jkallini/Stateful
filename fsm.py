import json
from automata.fa.dfa import DFA
from automata.fa.nfa import NFA


def parse_json(json_string):
    json.loads(json_string)
    dfa = DFA(
        states={'q0', 'q1'},
        input_symbols={'0', '1'},
        transitions={
            'q0': {'0': 'q0', '1': 'q1'},
            'q1': {'0': 'q1', '1': 'q1'}
        },
        initial_state='q0',
        final_states={'q0'}
    )
    dfa2 = DFA(
        states={'q0', 'q1', 'q2'},
        input_symbols={'0', '1'},
        transitions={
            'q0': {'0': 'q2', '1': 'q1'},
            'q1': {'0': 'q1', '1': 'q1'},
            'q2': {'0': 'q2', '1': 'q1'}
        },
        initial_state='q0',
        final_states={'q0', 'q1'}
    )

    print(equal(dfa, dfa2))

# Check if state q_i and q_j are equivalent. Returns True if
# q_i and q_j are both final states or both intermediate states,
# and false otherwise.
def equal_states(qi, qj, dfa1, dfa2):
    return bool(qi in dfa1.final_states) == bool(qj in dfa2.final_states)

def equal(fsm1, fsm2):

    # first check alphabet equivalence
    alpha1 = fsm1.input_symbols
    alpha2 = fsm2.input_symbols

    if alpha1 != alpha2:
        return False

    alphabet = alpha1

    # if FSMs are NFAs, convert them to DFAs
    if type(fsm1) is NFA:
        dfa1 = DFA.from_nfa(fsm1)
    else:
        dfa1 = fsm1
    if type(fsm2) is NFA:
        dfa2 = DFA.from_nfa(fsm2)
    else:
        dfa2 = fsm2
    
    # get minimal DFAs
    min_dfa1 = dfa1.minify()
    min_dfa2 = dfa2.minify()

    # begin with initial states
    q0 = min_dfa1.initial_state
    r0 = min_dfa2.initial_state
    inital_pair = (q0, r0)

    # maintain verified and unverfied states
    state_pairs = []
    visited_pairs = set()
    state_pairs.append(inital_pair)

    # iterate until there are no unverified pairs
    while len(state_pairs) != 0:

        # pop state pair, and check if equal
        qi, qj = state_pairs.pop()
        visited_pairs.add((qi, qj))
        if not equal_states(qi, qj, min_dfa1, min_dfa2):
            return False

        for sym in alphabet:
            ri = min_dfa1.transitions[qi][sym]
            rj = min_dfa2.transitions[qj][sym]
            new_pair = (ri, rj)
            if new_pair not in visited_pairs:
                state_pairs.append(new_pair)
    
    return True
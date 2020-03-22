import json
from automata.fa.dfa import DFA
from automata.fa.nfa import NFA

TEXT = 'text'
EPS = '\\epsilon'


# Get states, final states, and node-state map of the FSM.
def get_states(fsm):
    states = set()
    final_states = set()
    node_map = {}
    for i in range(0, len(fsm['nodes'])):
        n = fsm['nodes'][i]
        label = n[TEXT]

        # check if state is given a unique label
        if label == '':
            raise Exception("A state is missing a label!")
        if label in states:
            raise Exception("More than one state has label \"" + label + "\"!")
        states.add(label)

        # if accept state, add it to set of final states
        if n['isAcceptState']:
            final_states.add(label)

        # add index and state to mapping
        node_map[i] = label

    return states, final_states, node_map


# Get input alphabet of this fsm.
def get_alphabet(fsm, det):
    input_symbols = set()
    for l in fsm['links']:
        if l['type'] == 'Link' or l['type'] == 'SelfLink':
            if l[TEXT] == '':
                raise Exception("A transition is missing a label!")
            labels = l[TEXT].split(",")
            for label in labels:
                if label == '':
                    raise Exception("A transition has an invalid label!")
                if label == EPS:
                    if det:
                        raise Exception("A DFA should not have epsilon transitions!")
                    else:
                        label = ''
                input_symbols.add(label.strip())
    return input_symbols


def get_DFA_transitions(fsm, states, node_map, alphabet):

    transitions = {}
    for state in states:
        transitions[state] = {}

    initial_state = ''
    for l in fsm['links']:
        link_type = l['type']
        link_labels = l[TEXT].split(",")

        for label in link_labels:
            link_label = label.strip()

            # case 1: StartLink
            if link_type == "StartLink":
                # check if we've seen a start state before
                if initial_state != '':
                    raise Exception("More than one state is " +
                                    "labeled as the start state!")
                initial_state = node_map[l['node']]

            # case 2: SelfLink
            if link_type == "SelfLink":
                n = node_map[l['node']]
                if link_label in transitions[n]:
                    raise Exception("State " + n + " has more than one outgoing"
                                    + " transition labeled \"" + link_label + "\"!")
                transitions[n][link_label] = n

            # case 3: Link
            if link_type == "Link":
                n1 = node_map[l['nodeA']]
                n2 = node_map[l['nodeB']]
                if link_label in transitions[n1]:
                    raise Exception("State " + n1 + " has more than one outgoing"
                                    + " transition labeled \"" + link_label + "\"!")
                transitions[n1][link_label] = n2

    # verify that all states have transitions for each symbol
    for state, links in transitions.items():
        for symbol in alphabet:
            if symbol not in links:
                raise Exception("State " + state + " is missing a transition"
                                + " for symbol \"" + symbol + "\"!")

    return initial_state, transitions


def get_NFA_transitions(fsm, states, node_map, alphabet):

    transitions = {}
    for state in states:
        transitions[state] = {}

    initial_state = ''
    for l in fsm['links']:
        link_type = l['type']
        link_labels = l[TEXT].split(",")

        for label in link_labels:
            link_label = label.strip()

            # convert \epsilon to '' for automata library
            if link_label == EPS:
                link_label = ''

            # case 1: StartLink
            if link_type == "StartLink":
                # check if we've seen a start state before
                if initial_state != '':
                    raise Exception("More than one state is " +
                                    "labeled as the start state!")
                initial_state = node_map[l['node']]

            # case 2: SelfLink
            if link_type == "SelfLink":
                n = node_map[l['node']]
                if link_label not in transitions[n]:
                    transitions[n][link_label] = set()
                transitions[n][link_label].add(n)

            # case 3: Link
            if link_type == "Link":
                n1 = node_map[l['nodeA']]
                n2 = node_map[l['nodeB']]
                if link_label not in transitions[n1]:
                    transitions[n1][link_label] = set()
                transitions[n1][link_label].add(n2)

    return initial_state, transitions


def parse_json(json_string, det):
    fsm = json.loads(json_string)

    try:
        states, final_states, node_map = get_states(fsm)
        input_symbols = get_alphabet(fsm, det)
        if det:
            initial_state, transitions = \
                get_DFA_transitions(fsm, states, node_map, input_symbols)
        else:
            initial_state, transitions = \
                get_NFA_transitions(fsm, states, node_map, input_symbols)
    except Exception as e:
        return str(e)

    dfa = NFA(
        states=states,
        input_symbols=input_symbols,
        transitions=transitions,
        initial_state=initial_state,
        final_states=final_states
    )

    return "Initial State: " + dfa.initial_state + "\n" + \
        "Alphabet: " + str(dfa.input_symbols) + "\n" + \
            "States: " + str(dfa.states) + "\n" + \
                "Transitions: " + str(dfa.transitions) + "\n" + \
                    "Final States: " + str(dfa.final_states)

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
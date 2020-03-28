from automata.fa.dfa import DFA
from automata.fa.nfa import NFA
from fsm import equal


def main():
    fsm1 = NFA(states={'1', '2', '3', '4', '5'},
               input_symbols={'c', 'a', 't', 's', ''},
               transitions={'1': {'c': {'2'}}, '2': {'a': {'3'}}, '3': {
                   't': {'4'}}, '4': {'s': {'5'}}, '5': {}},
               initial_state='1',
               final_states={'4', '5'})
    fsm2 = NFA(states={'0','1', '2', '3', '4', '5'},
               input_symbols={'c', 'a', 't', 's', ''},
               transitions={'0': {'': {'1'}},  '1': {'c': {'2'}}, '2': {'a': {'3'}}, '3': {
                   't': {'4'}}, '4': {'s': {'5'}}, '5': {}},
               initial_state='0',
               final_states={'4', '5'})

    print(equal(fsm1, fsm2))

if __name__ == "__main__":
    main()

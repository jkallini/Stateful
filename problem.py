#!/usr/bin/env python

#-----------------------------------------------------------------------
# problem.py
# author: Julie Kallini
#-----------------------------------------------------------------------

from automata.fa.dfa import DFA

class Problem:

    def __init__(self, probid, description, fsm):
        self._id = probid
        self._description = description
        self._fsm = fsm
        self._deterministic = (type(fsm) == DFA)

    def __str__(self):
        return str(self._description)

    def get_id(self):
        return self._id

    def get_description(self):
        return self._description

    def is_deterministic(self):
        return self._deterministic

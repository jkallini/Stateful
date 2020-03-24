#!/usr/bin/env python

#-----------------------------------------------------------------------
# problem.py
# author: Julie Kallini
#-----------------------------------------------------------------------

from automata.fa.dfa import DFA

class Problem:

    def __init__(self, probid, description, probtype, fsm):
        self._id = probid
        self._description = description
        self._type = probtype
        self._fsm = fsm
        self._isDet = (type(fsm) == DFA)

    def __str__(self):
        return str(self._description)

    def get_id(self):
        return self._id

    def get_description(self):
        return self._description

    def get_type(self):
        return self._type

    def is_deterministic(self):
        return self._isDet

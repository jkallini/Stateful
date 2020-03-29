#!/usr/bin/env python

# -----------------------------------------------------------------------
# problem.py
# author: Julie Kallini
# -----------------------------------------------------------------------

from automata.fa.dfa import DFA


class Problem:

    EASY = 0
    MEDI = 1
    HARD = 2

    def __init__(self, probid, description, fsm, difficulty):
        self._id = probid
        self._description = description
        self._fsm = fsm
        self._deterministic = (type(fsm) == DFA)
        self._difficulty = difficulty

    def __str__(self):
        return str(self._description)

    def get_id(self):
        return self._id

    def get_fsm(self):
        return self._fsm

    def get_description(self):
        return self._description

    def is_deterministic(self):
        return self._deterministic

    def get_difficulty(self):
        return self._difficulty

#!/usr/bin/env python

#-----------------------------------------------------------------------
# problems.py
# author: Julie Kallini
#-----------------------------------------------------------------------

import fsm as FSM

problem_bank = {}

def get_problem_description(probid):
    return problem_bank[probid].description
#!/usr/bin/env python

# -----------------------------------------------------------------------
# run.py
# author: Julie Kallini
# -----------------------------------------------------------------------

from stateful import app
if __name__ == '__main__':
    app.run(port='5555', debug=True)
#!/usr/bin/env python

import subprocess
from flask import Flask, g

app = Flask(__name__)

def get_cows():
    """Returns a list of all the available cows
    This is the output to `cowsay -l`
    """
    cowsays = []
    cowsay_string = subprocess.check_output(['cowsay', '-l'])
    cowsay_lines = cowsay_string.split('\n')

    # the first line is not helpful
    cowsay_lines = cowsay_string[1:]

    cowsays = []
    for line in cowsay_lines:
        cows = line.split(' ')
        cowsays += cows

    return cowsays

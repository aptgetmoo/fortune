#!/usr/bin/env python

import subprocess
from random import choice
from flask import Flask, g

app = Flask(__name__)

def get_cows():
    """Returns a list of all the available cows
    This is the output to `cowsay -l`
    """

    if getattr(g, cows, None) is not None:
        return g.cows
    cowsays = []
    cowsay_string = subprocess.check_output(['cowsay', '-l'])
    cowsay_lines = cowsay_string.split('\n')

    # the first line is not helpful
    cowsay_lines = cowsay_lines[1:]

    cowsays = []
    for line in cowsay_lines:
        cows = line.split(' ')
        cowsays += cows

    g.cows = cowsays
    return cowsays


@app.route('/')
def index():
    fortune = subprocess.check_output(['fortune'])
    cowsay = subprocess.check_call(['cowsay', '-f', choice(get_cows()),
                                    fortune])

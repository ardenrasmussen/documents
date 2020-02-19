#!/usr/bin/env python3
import numpy as np
from tabulate import tabulate


class Automata(object):
    def __init__(self,
                 alphabet=['a', 'b'],
                 states=['q'],
                 initial=None,
                 accepting=[],
                 transition=lambda a, b: a,
                 notation='add'):
        self.alphabet = alphabet
        self.states = states
        self.initial = initial
        self.accepting = accepting
        self.transition = transition
        self.notation = notation

    def fmtword(self, word):
        if self.notation == 'add':
            return "+".join([str(w) for w in word])
        else:
            return "".join([str(w) for w in word])

    def fmtdot(self):
        print("digraph {")
        for state in self.states:
            for alpha in self.alphabet:
                print("  \"{}\"->\"{}\"[label=\"{}\"];".format(
                    state, self.transition(state, alpha), alpha))
        print("}")

    def fuzz(self, n=1, length=1):
        return np.random.choice(self.alphabet, (n, length), replace=True)

    def get_state(self, word):
        current_state = self.initial
        while len(word) != 0:
            current_state = self.transition(current_state, word[0])
            word = word[1:]
        return current_state

    def __call__(self, word):
        if self.get_state(word) in self.accepting:
            return True
        return False


z6z = Automata([+1, -1],
               states=[0, 1, 2, 3, 4, 5],
               initial=0,
               accepting=[0],
               transition=lambda a, b: (a + b) % 6)

z6z.fmtdot()

#!/usr/bin/env python

import unittest
from fortune import *

class TestGetCows(unittest.TestCase):
    def setUp(self):
        self.cows = get_cows()

    def test_cows_return_type():
        """Assert that we have a list of strings"""
        self.assertTrue(type(self.cows) == list)
        self.assertTrue(len(self.cows) > 0)
        self.assertTrue(all([type(c) == str for c in self.cows]))

    def test_cows_default():
        """Assert that the default cow (at least) exists"""
        self.assertTrue('default' in self.cows)

#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class MaxIntegerTest(unittest.TestCase):

    '''
    Test class for function max_integer
    '''
    def test_max_integer(self):
        '''
        Test method for checking correct output for
        given values
        '''

        self.assertAlmostEqual(max_integer([1, 2, 3]), 3)
        self.assertAlmostEqual(max_integer([5, 7, 9]), 9)
        self.assertAlmostEqual(max_integer([]), None)

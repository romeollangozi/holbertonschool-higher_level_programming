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
        Test method for checking correct output
        '''

        self.assertAlmostEqual(max_integer([1, 2, 3]), 3)
        self.assertAlmostEqual(max_integer([5, 7, 9]), 9)
        self.assertAlmostEqual(max_integer([]), None)
        self.assertAlmostEqual(max_integer([-1, -6, -5, -4]), -1)
        self.assertAlmostEqual(max_integer([-1, 3, 2, -4]), 3)
        self.assertAlmostEqual(max_integer([1, 5, 2.3, 5.7, 6.5]), 6.5)
        self.assertAlmostEqual(max_integer(), None)

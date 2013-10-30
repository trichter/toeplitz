#!/usr/bin/env python
# (C) 2013 Tom Richter
# MIT license

from numpy.random import random, seed
import numpy as np
import unittest
from toeplitz import sto_sl, cto_sl
SCIPY = True
try:
    import scipy.linalg
except ImportError:
    SCIPY = False
    from warnings import warn
    warn('toeplitz tests need scipy installed')

class UtilTestCase(unittest.TestCase):
    """
    test against scipy.linalg
    """
    def setUp(self):
        # set specific seed value such that random numbers are reproducible
        seed(42)

    def test_sto_sl(self):
        a1 = random(50) - 0.5
        a2 = random(50) - 0.5
        b = random(50) - 0.5
        toep2 = np.hstack((a1[0], a2[1:], a1[1:]))  # row, column
        x2 = sto_sl(toep2, b)
        if SCIPY:
            toep = scipy.linalg.toeplitz(a1, a2)  # column, row
            x = np.dot(scipy.linalg.inv(toep), b)
            np.testing.assert_array_almost_equal(x, x2, decimal=4)

    def test_cto_sl(self):
        a1 = random(50) - 0.5 + 0.1j * (random(50) - 0.5)
        a2 = random(50) - 0.5 + 0.1j * (random(50) - 0.5)
        b = random(50) - 0.5 + 0.05j * (random(50) - 0.5)
        toep2 = np.hstack((a1[0], a2[1:], a1[1:]))  # row, column
        x2 = cto_sl(toep2, b)
        if SCIPY:
            toep = scipy.linalg.toeplitz(a1, a2)  # column, row
            x = np.dot(scipy.linalg.inv(toep), b)
            np.testing.assert_array_almost_equal(x, x2, decimal=4)

def suite():
    return unittest.makeSuite(UtilTestCase, 'test')

if __name__ == '__main__':
    unittest.main(defaultTest='suite')

#!/usr/bin/env python
import unittest
from project.cumulative_sum import cumulative_sum


class TestCumulativeSum(unittest.TestCase):

    def test_csum(self):
        """Trivial test case."""
        self.assertEqual(cumulative_sum(5), 15)

    def test_errors(self):
        """Tst invalid parameters are handled as expected."""
        with self.assertRaises(TypeError):
            cumulative_sum("foobar")

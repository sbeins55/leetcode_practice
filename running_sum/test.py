import unittest

from running_sum.solution import running_sum


class RunningSumTest(unittest.TestCase):

    def test_empty(self):
        expected = []
        actual = running_sum([])
        self.assertEqual(expected, actual, msg="Output does match the expected solution")

    def test_simple(self):
        expected = [1, 3, 6, 10]
        actual = running_sum([1, 2, 3, 4])
        self.assertEqual(expected, actual, msg="Output does match the expected solution")

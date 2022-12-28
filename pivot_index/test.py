import unittest

from pivot_index.solution import pivot_index


class RunningSumTest(unittest.TestCase):

    def test_simple(self):
        expected = -1
        actual = pivot_index([1, 2, 3])
        self.assertEqual(expected, actual, msg="Output does match the expected solution")

    def test_with_positive_numbers(self):
        expected = 3
        actual = pivot_index([1, 7, 3, 6, 5, 6])
        self.assertEqual(expected, actual, msg="Output does match the expected solution")

    def test_with_negative_numbers(self):
        expected = 0
        actual = pivot_index([2, 1, -1])
        self.assertEqual(expected, actual, msg="Output does match the expected solution")

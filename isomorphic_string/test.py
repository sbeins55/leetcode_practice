import unittest

from solution import is_isomorphic


class IsIsomorphicTest(unittest.TestCase):

    def test_positive_simple(self):
        result = is_isomorphic("egg", "add")
        self.assertTrue(result, msg="Output does match the expected solution")

    def test_positive_complex(self):
        result = is_isomorphic("paper", "title")
        self.assertTrue(result, msg="Output does match the expected solution")

    def test_negative_simple(self):
        result = is_isomorphic("foo", "bar")
        self.assertFalse(result, msg="Output does match the expected solution")

    def test_negative_complex(self):
        result = is_isomorphic("bbbaaaba", "aaabbbba")
        self.assertFalse(result, msg="Output does match the expected solution")
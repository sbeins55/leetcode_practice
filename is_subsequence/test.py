import unittest
from solution import is_subsequence


class IsSubsequenceTest(unittest.TestCase):

    def test_postive_empty(self):
        s = ""
        t = "alkdjfak"
        result = is_subsequence(s, t)
        self.assertTrue(result)

    def test_postive_connected(self):
        s = "abc"
        t = "kkkabcjfja"
        result = is_subsequence(s, t)
        self.assertTrue(result)

    def test_positive_scattered(self):
        s = "abc"
        t = "ajfhbquecivk"
        result = is_subsequence(s, t)
        self.assertTrue(result)

    def test_negative_no_common(self):
        s = "abc"
        t = "def"
        result = is_subsequence(s, t)
        self.assertFalse(result)

    def test_negative_unordered(self):
        s = "abc"
        t = "cab"
        result = is_subsequence(s, t)
        self.assertFalse(result)


import unittest

from longest_palindrome.solution import longest_palindrome


class LongestPalindromeTest(unittest.TestCase):

    def test_palindrome_with_no_letters(self):
        result = longest_palindrome("")
        self.assertEqual(0, result)

    def test_palindrome_with_one_letter(self):
        result = longest_palindrome("a")
        self.assertEqual(1, result)

    def test_palindrome_with_all_letters_used(self):
        result = longest_palindrome("aabbccdddd")
        self.assertEqual(10, result)

    def test_palindrome_with_some_letters_used(self):
        result = longest_palindrome("abbcdddd")
        self.assertEqual(7, result)

    def test_palindrome_with_all_same_letters(self):
        result = longest_palindrome("aaaaaaaaaaaa")
        self.assertEqual(12, result)

    def test_palindrome_with_all_different_letters(self):
        result = longest_palindrome("abcdefghijklmnopqrstuvwxyz")
        self.assertEqual(1, result)
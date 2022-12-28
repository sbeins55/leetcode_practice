import unittest

from binary_search.solution import search


class BinarySearchTest(unittest.TestCase):

    def test_one_element(self):
        nums = [1]
        target = 1
        expected = 0
        actual = search(nums, target)
        self.assertEqual(expected, actual)

    def test_even_elements(self):
        nums = [1, 2, 3, 4]
        target = 3
        expected = 2
        actual = search(nums, target)
        self.assertEqual(expected, actual)

    def test_odd_elements(self):
        nums = [1, 2, 3, 4, 5]
        target = 3
        expected = 2
        actual = search(nums, target)
        self.assertEqual(expected, actual)

    def test_with_negative_numbers(self):
        nums = [-9, -5, -1, 3, 7, 11]
        target = 3
        expected = 3
        actual = search(nums, target)
        self.assertEqual(expected, actual)

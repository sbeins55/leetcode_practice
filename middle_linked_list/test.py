import unittest

from middle_linked_list.solution import middle_linked_list
from data_structures.classes import ListNode


class MiddleLinkedListTest(unittest.TestCase):

    def test_empty(self):
        head = None
        actual = middle_linked_list(head)
        expected = None

        self.assertEqual(expected, actual)

    def test_odd(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        actual = middle_linked_list(head)
        expected = ListNode(3)

        self.assertEqual(expected.val, actual.val)

    def test_even(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
        actual = middle_linked_list(head)
        expected = ListNode(4)

        self.assertEqual(expected.val, actual.val)

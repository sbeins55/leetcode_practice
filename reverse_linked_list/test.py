import unittest

from reverse_linked_list.solution import reverse_linked_list
from data_structures.classes import ListNode
from helpers.utils import linked_list_to_list


class ReverseLinkedListTest(unittest.TestCase):

    def test_empty(self):
        head = None
        result = reverse_linked_list(head)

        expected = []
        actual = linked_list_to_list(result)

        self.assertEqual(expected, actual)

    def test_two(self):
        head = ListNode(1, ListNode(2))
        result = reverse_linked_list(head)

        expected = [2, 1]
        actual = linked_list_to_list(result)

        self.assertEqual(expected, actual)

    def test_simple(self):
        head = ListNode(1, ListNode(2, ListNode(3)))
        result = reverse_linked_list(head)

        expected = [3, 2, 1]
        actual = linked_list_to_list(result)

        self.assertEqual(expected, actual)

    def test_large(self):
        cur = head = ListNode(1)
        for i in range(2, 1001):
            cur.next_node = ListNode(i)
            cur = cur.next_node

        result = reverse_linked_list(head)

        expected = [i for i in range(1000, 0, -1)]
        actual = linked_list_to_list(result)

        self.assertEqual(expected, actual)

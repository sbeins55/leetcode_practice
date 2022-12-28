import unittest

from data_structures.classes import ListNode
from helpers.utils import linked_list_to_list
from merge_sorted_lists.solution import merge_sorted_lists


class MergedSortedListsTest(unittest.TestCase):

    def test_empty(self):
        list1 = None
        list2 = None
        head = merge_sorted_lists(list1, list2)

        expected = []
        actual = linked_list_to_list(head)

        self.assertEqual(expected, actual)

    def test_single(self):
        list1 = None
        list2 = ListNode(0)
        head = merge_sorted_lists(list1, list2)

        expected = [0]
        actual = linked_list_to_list(head)

        self.assertEqual(expected, actual)

    def test_simple(self):
        list1 = ListNode(1, ListNode(2, ListNode(4)))
        list2 = ListNode(1, ListNode(3, ListNode(4)))
        head = merge_sorted_lists(list1, list2)

        expected = [1, 1, 2, 3, 4, 4]
        actual = linked_list_to_list(head)

        self.assertEqual(expected, actual)

import unittest

from data_structures.classes import ListNode
from detect_cycle.solution import detect_cycle


class DetectCycleTest(unittest.TestCase):

    def test_no_cycle(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
        expected = None
        actual = detect_cycle(head)

        self.assertEqual(expected, actual)

    def test_cycle_at_start(self):
        head = ListNode(1)
        cycle = ListNode(2, ListNode(3, ListNode(4, head)))
        head.next_node = cycle

        expected = 1
        actual = detect_cycle(head)

        self.assertEqual(expected, actual.val)

    def test_cycle_at_middle(self):
        head = ListNode(1, ListNode(2, ListNode(3)))
        cycle = ListNode(4, ListNode(5, head.next_node.next_node))
        head.next_node.next_node.next_node = cycle

        expected = 3
        actual = detect_cycle(head)

        self.assertEqual(expected, actual.val)

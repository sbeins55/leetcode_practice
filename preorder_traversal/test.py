import unittest

from data_structures.classes import Node
from preorder_traversal.solution import preorder


class PreorderTraversalTest(unittest.TestCase):

    def test_simple(self):
        root = Node(1, [Node(3, [Node(5, []), Node(6, [])]), Node(2, []), Node(4, [])])

        expected = [1, 3, 5, 6, 2, 4]
        actual = preorder(root)

        self.assertEqual(expected, actual)

    def test_complex(self):
        root = Node(
            1,
            [
                Node(2, []),
                Node(3, [
                    Node(6, []),
                    Node(7, [
                        Node(11, [
                            Node(14, [])
                        ])
                    ])
                ]),
                Node(4, [
                    Node(8, [
                        Node(12, [])
                    ])
                ]),
                Node(5, [
                    Node(9, [
                        Node(13, [])
                    ]),
                    Node(10, [])
                ]),
            ]
        )

        expected = [1, 2, 3, 6, 7, 11, 14, 4, 8, 12, 5, 9, 13, 10]
        actual = preorder(root)

        self.assertEqual(expected, actual)

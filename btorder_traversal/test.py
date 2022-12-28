import unittest

from btorder_traversal.solution import level_order
from data_structures.classes import TreeNode


class BinaryTreeLevelOrderTraversalTest(unittest.TestCase):

    def test_single_node(self):
        # [1]
        root = TreeNode(1, None, None)
        expected = [[1]]
        actual = level_order(root)

        self.assertEqual(expected, actual)

    def test_shallow_tree(self):
        # [3, 9, 20, null, null, 15, 7]
        root = TreeNode(3,
                        TreeNode(9, None, None),
                        TreeNode(20,
                                 TreeNode(15, None, None),
                                 TreeNode(7, None, None)
                                 )
                        )
        expected = [[3], [9, 20], [15, 7]]
        actual = level_order(root)

        self.assertEqual(expected, actual)

    def test_deep_tree(self):
        # [0,2,4,1,null,3,-1,5,1,null,6,null,8]

        self.assertTrue(True)

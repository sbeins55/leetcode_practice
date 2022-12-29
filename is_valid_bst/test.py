import unittest

from data_structures.classes import TreeNode
from is_valid_bst.solution import is_valid_bst


class IsValidBstTest(unittest.TestCase):

    def test_single_node(self):
        root = TreeNode(1, None, None)
        self.assertTrue(is_valid_bst(root))

    def test_multiple_nodes_valid(self):
        root = TreeNode(2, TreeNode(1, None, None), TreeNode(3, None, None))
        self.assertTrue(is_valid_bst(root))

    def test_multiple_nodes_invalid(self):
        root = TreeNode(1, TreeNode(2, None, None), TreeNode(3, None, None))
        self.assertFalse(is_valid_bst(root))

    def test_same_nodes_invalid(self):
        root = TreeNode(1, TreeNode(1, None, None), TreeNode(1, None, None))
        self.assertFalse(is_valid_bst(root))

    def test_large_depth_valid(self):
        root = TreeNode(7,
                        TreeNode(3,
                                 TreeNode(2, TreeNode(1, None, None), None),
                                 TreeNode(5, TreeNode(4, None, None), TreeNode(6, None, None))
                                 ),
                        TreeNode(11,
                                 TreeNode(9, TreeNode(8, None, None), TreeNode(10, None, None)),
                                 TreeNode(13, TreeNode(12, None, None), TreeNode(14, None, None))
                                 )
                        )
        self.assertTrue(is_valid_bst(root))

    def test_large_depth_invalid(self):
        root = TreeNode(7,
                        TreeNode(3,
                                 TreeNode(2, TreeNode(1, None, None), None),
                                 TreeNode(9, TreeNode(5, None, None), TreeNode(11, None, None))
                                 ),
                        TreeNode(11,
                                 TreeNode(5, TreeNode(4, None, None), TreeNode(6, None, None)),
                                 TreeNode(13, TreeNode(12, None, None), TreeNode(14, None, None))
                                 )
                        )
        self.assertFalse(is_valid_bst(root))

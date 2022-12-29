import unittest

from data_structures.classes import TreeNode
from lowest_common_ancestor.solution import lowest_common_ancestor


class LowestCommonAncestorTest(unittest.TestCase):

    def test_simple(self):
        q = TreeNode(1, None, None)
        root = TreeNode(2, q, None)
        actual = lowest_common_ancestor(root, root, q)

        self.assertEqual(root, actual)

    def test_root_lca(self):
        p = TreeNode(2,
                     TreeNode(0, None, None),
                     TreeNode(4,
                              TreeNode(3, None, None),
                              TreeNode(5, None, None)
                              )
                     )
        q = TreeNode(8,
                     TreeNode(7, None, None),
                     TreeNode(9, None, None)
                     )
        root = TreeNode(6, p, q)
        actual = lowest_common_ancestor(root, p, q)

        self.assertEqual(root, actual)

    def test_second_level_lca(self):
        q = TreeNode(4, TreeNode(3, None, None), TreeNode(5, None, None) )
        p = TreeNode(2, TreeNode(0, None, None), q)
        root = TreeNode(6, p, TreeNode(8, TreeNode(7, None, None), TreeNode(9, None, None)))

        actual = lowest_common_ancestor(root, p, q)

        self.assertEqual(p, actual)

def lowest_common_ancestor(root, p, q):
    """
    Given a BST, find the lowest common ancestor (LCA) node of two given nodes in the BST.

    :param root: the root node of a BST
    :param p: a node in the BST
    :param q: a node in the BST
    :return: the lowest common ancestor between p and q in the BST
    """
    low = min(p.val, q.val)
    high = max(p.val, q.val)
    while root:
        if root.val > high:
            root = root.left
        elif root.val < low:
            root = root.right
        else:
            return root
    return None

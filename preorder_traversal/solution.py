def preorder(root):
    """
    Given the root of an n-ary tree, return the preorder traversal of its nodes' values.

    :param root: the start of the n-ary tree
    :return: the preorder traversal number of each of the nodes in the tree
    """
    if root is None:
        return []

    preorders = []
    stack = [root]

    while len(stack):
        node = stack.pop()
        preorders.append(node.val)
        stack.extend(node.children[::-1])

    return preorders

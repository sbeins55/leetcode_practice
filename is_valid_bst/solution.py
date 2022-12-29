from math import inf


def is_valid_bst(root):
    """
    Given the root of a binary tree, determine if it is a valid binary search tree (BST).


    :param root: the root of a binary tree
    :return: a boolean indicating whether the binary tree is valid
    """
    valid = True
    stack = [(root, -inf, inf)]

    while len(stack):
        node, low, high = stack.pop()

        if node is None:
            continue

        if node.val <= low or node.val >= high:
            valid = False
            break

        stack.append((node.right, node.val, high))
        stack.append((node.left, low, node.val))

    return valid

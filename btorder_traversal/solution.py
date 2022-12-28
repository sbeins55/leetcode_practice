def level_order(root):
    """
    Given the root of a binary tree, return the level order traversal of its nodes' values.

    :param root: the root of a binary tree
    :return: the level order traversal of the nodes in the binary tree
    """
    if root is None:
        return []

    stack = [(root, 0)]
    output = [[root.val]]
    while len(stack):
        node, level = stack.pop()

        out = output[level + 1] if level + 1 < len(output) else []
        if node.right:
            stack.append((node.right, level + 1))

        if node.left:
            stack.append((node.left, level + 1))

        if node.left:
            out.append(node.left.val)

        if node.right:
            out.append(node.right.val)

        if node.left or node.right:
            if level + 1 < len(output):
                output[level + 1] = out
            else:
                output.append(out)

    return output

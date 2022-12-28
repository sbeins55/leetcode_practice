def linked_list_to_list(head):
    """
    Given the head node of a linked list, return a list of values

    :param head: the first node in a linked list
    :return: a list of values in the linked list
    """
    if head is None:
        return []

    res = [head.val]
    while head.next_node:
        head = head.next_node
        res.append(head.val)

    return res

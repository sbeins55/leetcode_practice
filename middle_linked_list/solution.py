def middle_linked_list(head):
    """
    Given a linked list return the middle element.

    :param head: the beginning node of a linked list
    :return: the middle element of the linked list
    """
    slow = fast = head
    while fast and fast.next_node:
        slow = slow.next_node
        fast = fast.next_node.next_node

    return slow
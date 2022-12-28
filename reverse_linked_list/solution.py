from data_structures.classes import ListNode


def reverse_linked_list(head):
    """
    Given the head of a singly linked list, reverse the list, and return the reversed list.

    :param head: the starting point of a linked list
    :return: the head of the linked list, the last element of the original
    """
    if not head:
        return head

    cur = prev = ListNode(head.val, None)
    while head.next_node:
        head = head.next_node
        cur = ListNode(head.val, prev)
        prev = cur

    return cur

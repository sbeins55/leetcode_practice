from data_structures.classes import ListNode


def merge_sorted_lists(list1, list2):
    """
    Given the heads of two sorted linked lists, merge the two lists into one sorted list.

    :param list1: the head of the first sorted linked list
    :param list2: the head of the second sorted linked list
    :return: the head of the merged linked list
    """
    cur = dummy = ListNode()
    while list1 and list2:
        if list1.val < list2.val:
            cur.next_node = list1
            list1, cur = list1.next_node, list1
        else:
            cur.next_node = list2
            list2, cur = list2.next_node, list2

    if list1 or list2:
        cur.next_node = list1 if list1 else list2

    return dummy.next_node

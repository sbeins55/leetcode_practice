def detect_cycle(head):
    """
    Given the head of a linked list, return the node where the cycle begins.

    :param head: the start node of a linked list
    :return: the node where a cycle begins or null if no cycle exists
    """
    cycle = False
    slow = fast = head
    while fast and fast.next_node:
        slow, fast = slow.next_node, fast.next_node.next_node
        if fast == slow:
            cycle = True
            break

    if not cycle:
        return None

    while head != slow:
        head, slow = head.next_node, slow.next_node

    return head
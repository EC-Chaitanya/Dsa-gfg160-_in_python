def buildLinkedList(values, pos):
    if not values:
        return None

    head = Node(values[0])
    curr = head
    loop_node = None

    for i in range(1, len(values)):
        curr.next = Node(values[i])
        curr = curr.next
        if i + 1 == pos:
            loop_node = curr

    # Create loop if pos > 0
    if pos == 1:
        loop_node = head
    if pos > 0:
        curr.next = loop_node

    return head

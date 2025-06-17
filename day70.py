class Node:
    def __init__(self, val, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head):
        if not head:
            return None

        # Step 1: Create new nodes and insert them after original nodes
        curr = head
        while curr:
            new_node = Node(curr.val)
            new_node.next = curr.next
            curr.next = new_node
            curr = new_node.next

        # Step 2: Assign random pointers to the copied nodes
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        # Step 3: Separate the copied list from the original list
        curr = head
        pseudo_head = Node(0)
        copy_curr = pseudo_head

        while curr:
            front = curr.next.next

            # Extract the copied node
            copy = curr.next
            copy_curr.next = copy
            copy_curr = copy

            # Restore the original list
            curr.next = front
            curr = front

        return pseudo_head.next

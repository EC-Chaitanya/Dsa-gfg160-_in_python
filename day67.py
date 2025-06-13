class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class Solution:
    def sortedMerge(self, head1, head2):
        # Dummy node to start the merged list
        dummy = Node(0)
        tail = dummy

        # While both lists are non-empty
        while head1 and head2:
            if head1.data <= head2.data:
                tail.next = head1
                head1 = head1.next
            else:
                tail.next = head2
                head2 = head2.next
            tail = tail.next

        # Append the remaining part of the non-empty list
        if head1:
            tail.next = head1
        elif head2:
            tail.next = head2

        return dummy.next  # First node after dummy

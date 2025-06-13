class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        curr = head
        count = 0
        
        # First check how many nodes we have in this group
        while curr and count < k:
            curr = curr.next
            count += 1
        
        # If we have at least 1 node, reverse the group
        if count > 0:
            prev = None
            curr = head
            nxt = None
            i = 0
            while i < count:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
                i += 1
            # After reversing, head becomes tail of this group, connect it to next reversed group
            head.next = self.reverseKGroup(curr, k)
            return prev
        else:
            return head

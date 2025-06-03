#function Template for python3

"""
# Node Class

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

"""

class Solution:
    def reverseList(self, head):
        # Code here
        prev = None
        current = head
        while current:
            n_node = current.next
            current.next = prev
            prev = current
            current = n_node
        return prev

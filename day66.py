# Your task is to complete this function

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''


class Solution:
    
    #Function to rotate a linked list.
    def rotate(self, head, k):
        if not head or k == 0:
            return head
        l = 1
        tail = head
        while tail.next:
            tail = tail.next
            l += 1
        tail.next = head
        k = k% l
        if k== 0:
            tail.next = None
            return head
        new_tail = head
        for _ in range(k -1):
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None
        return new_head

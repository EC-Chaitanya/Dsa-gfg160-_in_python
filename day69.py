class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def reverse(self, head):
        prev = None
        while head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        return prev

    def addTwoLists(self, first, second):
        # Step 1: Reverse both lists
        first = self.reverse(first)
        second = self.reverse(second)

        carry = 0
        dummy = Node(0)
        curr = dummy

        # Step 2: Add digit by digit
        while first or second or carry:
            val1 = first.data if first else 0
            val2 = second.data if second else 0

            total = val1 + val2 + carry
            carry = total // 10
            curr.next = Node(total % 10)
            curr = curr.next

            if first:
                first = first.next
            if second:
                second = second.next

        # Step 3: Reverse the result list
        result = self.reverse(dummy.next)

        # Step 4: Remove leading zeros (if any)
        while result and result.data == 0 and result.next:
            result = result.next

        return result

import heapq
class Node:
    def _init_(self,x):
        self.data = x
        self.next = None
    def __lt__(self,other):
        return self.data < other.data

class Solution:
    def mergeKLists(self, arr):
        # code here
        # return head of merged list
        mh= []
        for node in arr:
            if node:
                heapq.heappush(mh, node)
        dummy = Node(0)
        current = dummy
        while mh:
            s = heapq.heappop(mh)
            current.next = s
            current = current.next
            if s.next:
                heapq.heappush(mh, s.next)
        return dummy.next

'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def inOrder(self,root):
        result =[]
        c = root
        while c:
            if c.left is None:
                result.append(c.data)
                c = c.right
            else:
                pre = c.left
                while pre.right and pre.right != c:
                    pre = pre.right
                if pre.right is None:
                    pre.right = c
                    c = c.left
                else:
                    pre.right = None
                    result.append(c.data)
                    c = c.right
        return result

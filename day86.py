'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def boundaryTraversal(self, root):
        if not root:
            return []
        result = []
        def  isLeaf(node):
            return node.left is None and node.right is None
        def addlb(node):
            curr = node.left
            while curr:
                if not isLeaf(curr):
                    result.append(curr.data)
                if curr.left:
                    curr = curr.left
                else:
                    curr = curr.right
        def addl(node):
            if node is None:
                return
            if isLeaf(node):
                result.append(node.data)
            addl(node.left)
            addl(node.right)
        def addrb(node):
            curr = node.right
            tmp = []
            while curr:
               if not isLeaf(curr):
                   tmp.append(curr.data)
               if curr.right:
                   curr= curr.right
               else:
                   curr= curr.left
            result.extend(reversed(tmp))
        if not isLeaf(root):
            result.append(root.data)
        addlb(root)
        addl(root)
        addrb(root)
        return result

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.count = 0
        self.result = -1

    def KthSmallestElement(self, root, K):
        def inorder(node):
            if not node or self.count >= K:
                return
            inorder(node.left)
            self.count += 1
            if self.count == K:
                self.result = node.data
                return
            inorder(node.right)
        
        inorder(root)
        return self.result

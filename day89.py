class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def isBST(self, root):
        def helper(node, min_val, max_val):
            if not node:
                return True
            if not (min_val < node.data < max_val):
                return False
            return (helper(node.left, min_val, node.data) and
                    helper(node.right, node.data, max_val))
        
        return helper(root, float('-inf'), float('inf'))

'''
# Tree Node
class Node:

    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def __init__(self):
        self.maxD = 0
    def diameter(self, root):
        def dfs(node):
            if not node:
                return 0
            leftH = dfs(node.left)
            rightH = dfs(node.right)
            self.maxD = max(self.maxD, leftH + rightH)
            return 1 + max(leftH, rightH)
        dfs(root)
        return self.maxD
        

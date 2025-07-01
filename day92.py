"""
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
"""
class Solution:
    def levelOrder(self, root):
        # Your code here
        if root is None:
            return []
        res = []
        que = [root]
        while que:
            levelSize = len(que)
            currLevel = []
            for _ in range(levelSize):
                node = que.pop(0)
                currLevel.append(node.data)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            res.append(currLevel)
        return res
        
        

'''
# Node class
class Node:
    def __init__(self,val):
        self.data = val
        self.right = None
        self.left = None

'''
# Note: Build tree and return root node
class Solution:
    def buildTree(self, inorder, preorder):
        if not preorder or not inorder:
            return None
        inMap = {val: idx for idx, val in enumerate(inorder)} 
        preIdx = [0]
        def helper(inSt, inEnd):
            if inSt > inEnd:
                return None
            rootV = preorder[preIdx[0]]
            root = Node(rootV)
            preIdx[0] += 1
            inIdx = inMap[rootV]
            root.left = helper(inSt, inIdx -1 )
            root.right =  helper(inIdx + 1, inEnd)
            return root
        return helper(0, len(inorder)- 1)

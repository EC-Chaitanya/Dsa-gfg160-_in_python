class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

class Solution:
    def LCA(self, root, n1, n2):
        # Base Case
        if not root:
            return None
        
        # If both nodes are smaller than root, LCA is in left subtree
        if n1 < root.data and n2 < root.data:
            return self.LCA(root.left, n1, n2)

        # If both nodes are greater than root, LCA is in right subtree
        if n1 > root.data and n2 > root.data:
            return self.LCA(root.right, n1, n2)

        # If one is on left and one is on right, root is LCA
        return root

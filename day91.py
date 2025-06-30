class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def findTarget(self, root, target):
        # Helper function for in-order traversal
        def inorder(node, elements):
            if node:
                inorder(node.left, elements)
                elements.append(node.data)
                inorder(node.right, elements)

        # Get sorted values from BST
        elements = []
        inorder(root, elements)

        # Two pointer approach
        left, right = 0, len(elements) - 1
        while left < right:
            current_sum = elements[left] + elements[right]
            if current_sum == target:
                return True
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        return False

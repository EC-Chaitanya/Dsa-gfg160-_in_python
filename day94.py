class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.index = 0

    # Function to serialize the tree into a list
    def serialize(self, root):
        arr = []
        
        def preorder(node):
            if node is None:
                arr.append(-1)
                return
            arr.append(node.data)
            preorder(node.left)
            preorder(node.right)
        
        preorder(root)
        return arr

    # Function to deserialize the list back into a tree
    def deSerialize(self, arr):
        def build():
            if self.index >= len(arr) or arr[self.index] == -1:
                self.index += 1
                return None
            node = Node(arr[self.index])
            self.index += 1
            node.left = build()
            node.right = build()
            return node
        
        return build()

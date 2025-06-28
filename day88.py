class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root, k):
        def dfs(node, current_sum, prefix_sum_count):
            if not node:
                return 0

            current_sum += node.data
            count = prefix_sum_count.get(current_sum - k, 0)

            prefix_sum_count[current_sum] = prefix_sum_count.get(current_sum, 0) + 1
            count += dfs(node.left, current_sum, prefix_sum_count)
            count += dfs(node.right, current_sum, prefix_sum_count)
            prefix_sum_count[current_sum] -= 1  # backtrack

            return count

        prefix_sum_count = {0: 1}  # sum of 0 has occurred once (base case)
        return dfs(root, 0, prefix_sum_count)

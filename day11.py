class Solution:
    def maxProduct(self, arr):
        """
        Find the maximum product of a subarray within the given array.

        Args:
            arr (list): The input array.

        Returns:
            int: The maximum product of a subarray.
        """
        if not arr:
            return 0

        max_product = arr[0]
        min_product = arr[0]
        result = arr[0]

        for i in range(1, len(arr)):
            current_num = arr[i]
            temp_max = max(current_num, current_num * max_product, current_num * min_product)
            temp_min = min(current_num, current_num * max_product, current_num * min_product)

            max_product = temp_max
            min_product = temp_min

            result = max(result, max_product)

        return result


# Driver Code
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr)
        print(ans)
        tc -= 1
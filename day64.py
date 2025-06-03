#User function Template for python3

class Solution:
    def productExceptSelf(self, arr):
        #code here
        n = len(arr)
        if n == 0:
            return []
        res = [1] * n
        prefix = 1
        for i in range(n):
            res[i] =prefix
            prefix *= arr[i]
        suffix = 1 
        for i in range(n-1, -1, -1):
            res[i] *= suffix
            suffix *= arr[i]
        return res

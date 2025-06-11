#User function Template for python3
class Solution:
    def subarraySum(self, arr, target):
        # code here
        s = 0
        cs = 0
        for end in range(len(arr)):
            cs += arr[end]
            while cs > target and s <= end:
                cs -= arr[s]
                s += 1
            if cs == target:
                return [s + 1, end +1]
        return [-1]

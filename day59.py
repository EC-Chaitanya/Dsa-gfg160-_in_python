#User function Template for python3


class Solution:
    def maxWater(self, arr):
        # code here
        if not arr or len(arr)< 3:
            return 0
        l , r = 0 , len(arr) - 1
        lm , rm = arr[l], arr[r]
        t = 0 
        while l < r:
            if arr[l] < arr[r]:
                l += 1
                lm = max(lm , arr[l])
                t  += max(0, lm - arr[l])
            else:
                r -= 1
                rm = max(rm , arr[r])
                t += max(0, rm - arr[r])
        return t

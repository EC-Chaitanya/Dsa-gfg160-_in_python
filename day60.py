
class Solution:
    def maxWater(self, arr):
        # code here
        n = len(arr)
        if n<2:
            return 0
        l = 0
        r = n-1
        max_area = 0
        while l < r:
             h = min(arr[l], arr[r])
             w = r - l
             a = h *w
             max_area = max(max_area, a)
             if arr[l] < arr[r]:
                 l += 1
             else:
                r -= 1
        return max_area

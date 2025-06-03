class Solution:
    def maxLen(self, arr):
        # code here
        arr = [ -1 if x == 0 else 1 for x in arr]
        prefix = 0
        maxl = 0
        sumi = {0: -1}
        for i, num in enumerate(arr):
            prefix += num
            if prefix in sumi:
                maxl = max(maxl, i - sumi[prefix])
            else:
                sumi[prefix] = i 
        return maxl

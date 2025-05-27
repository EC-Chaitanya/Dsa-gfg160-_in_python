#User function Template for python3

class Solution:
    def longestUniqueSubstr(self, s):
        # code here
        n = len(s)
        char = set()
        l = 0
        max_len = 0 
        for r in range(n):
            while s[r] in char:
                char.remove(s[l])
                l +=1
            char.add(s[r])
            max_len = max(max_len, r - l +1)
        return max_len
                

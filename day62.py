# User function Template for python3

class Solution:
    def longestSubarray(self, arr, k):  
        # code here
        p = 0
        l = 0
        ind = { }
        for i in range(len(arr)):
            p += arr[i]
            if p == k :
                l = i+ 1
            if ( p -k) in ind:
                l = max(l, i - ind[p - k])
            if p not in ind:
                ind[p] = i
        return l
    

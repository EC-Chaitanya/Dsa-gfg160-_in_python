# User function Template for python3

class Solution:
    #Function to find equilibrium point in the array.
    def findEquilibrium(self, arr):
        # code here
        t = sum(arr)
        l = 0
        for i in range(len(arr)):
            if l ==(t- l - arr[i]):
                return i
            l += arr[i]
        return -1
        


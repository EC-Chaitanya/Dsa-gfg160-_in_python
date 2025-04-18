class Solution:
    def maxSubArraySum(self, arr):
        # Your code here
        a = float("-inf")
        b = float("-inf")
        for i in range(0 , len(arr)):
            a = max(arr[i], a+arr[i])
            b = max(a,b)
        return b    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        ob = Solution()

        print(ob.maxSubArraySum(arr))
        print("~")
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
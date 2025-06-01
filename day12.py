#User function Template for python3

#Complete this function
#Function to find maximum circular subarray sum.
def circularSubarraySum(arr):
    ##Your code here
    def kadane_max(arr):
        max_ending = max_so_far = arr[0]
        for x in arr[1:]:
            max_ending = max(x, max_ending + x)
            max_so_far = max(max_so_far, max_ending)
        return max_so_far
    def kadane_min(arr):
        min_ending = min_so_far = arr[0]
        for x in arr[1:]:
            min_ending = min(x, min_ending + x)
            min_so_far = min(min_so_far, min_ending)
        return min_so_far
    total_sum = sum(arr)
    max_normal = kadane_max(arr)
    min_subarray = kadane_min(arr)
    
    if max_normal < 0:
        return max_normal
    else:
        return max(max_normal, total_sum- min_subarray)
    

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
import sys

if __name__ == "__main__":
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        print(circularSubarraySum(arr))

        T -= 1
        print("~")

# } Driver Code Ends

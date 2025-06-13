#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


# } Driver Code Ends

#User function Template for python3
class Solution:
    def findTriplets(self, arr):
        # Your code here
        n = len(arr)
        re = set()
        va = {}
        for i, v in enumerate(arr):
            va.setdefault(v,[]).append(i)
        for j in range(n):
            se = {}
            for k in range(j+1, n):
                t = - (arr[j] +arr[k])
                if t in se:
                    for l in se[t]:
                        trip = tuple(sorted([j,k,l]))
                        re.add(trip)
                se.setdefault(arr[k], []).append(k)
        
                        

        return sorted(re)

           


#{ 
 # Driver Code Starts.

def main():
    T = int(input())
    while (T > 0):

        A = [int(x) for x in input().strip().split()]

        ob = Solution()
        res = ob.findTriplets(A)
        res = sorted(res)
        if len(res) == 0:
            print('[]')
        for i in range(len(res)):
            for j in range(len(res[i])):
                print(res[i][j], end=" ")
            print("")
        print('~')
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
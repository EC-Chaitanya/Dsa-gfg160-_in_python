#User function Template for python3

class Solution:
    #Function to count the number of possible triangles.
    def countTriangles(self, arr):
        # code here
        n =  len(arr)
        arr.sort()
        c = 0
        for k in range(n- 1, 1, -1):
            i = 0
            j = k - 1
            while i < j:
                if arr[i] + arr[j] > arr[k]:
                    c += j - i
                    j -= 1 
                else:
                    i += 1
        return c

#User function Template for python3
class Solution:
    def kthMissing(self, arr, k):
        # code here
        m = 1
        c = 0
        i = 0
        while c < k:
            if i< len(arr) and arr[i] == m:
                i += 1
            else:
                c += 1
                if c == k:
                    return m
            m += 1
        return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.kthMissing(A, D)
        print(ans)
        print("~")

# } Driver Code Ends
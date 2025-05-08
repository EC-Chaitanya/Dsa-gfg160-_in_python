class Solution:
    
    #Function to find minimum number of pages.
    def findPages(self, arr, k):
        if k > len(arr):
             return -1
        def a(l):
            s, t = 1, 0
            for page in arr:
                t += page
                if t > l:
                    s += 1
                    t = page
                    if s > k:
                        return False
            return True
            
        l = max(arr)
        h = sum(arr)
        while l < h:
            mid = (l + h )// 2
            if a(mid):
                h = mid
            else:
                l = mid + 1
        return l
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3
import bisect
#Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.findPages(A, D)
        print(ans)
        print("~")

# } Driver Code Ends
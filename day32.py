#User function Template for python3


class Solution:

    def kthElement(self, a, b, k):
        n , m = len(a), len(b)
        if n > m:
            return self.kthElement(b, a, k)
        l = max(0, k -m)
        h = min(k, n)
        while l <= h:
            c1 = (l + h)//2
            c2 = k - c1
            if c2 >m or c2 < 0:
                if c2 >m:
                    l = c1+ 1
                else:
                    h = c1 -1
                continue
            l1 = float('-inf') if c1 == 0 else a[c1 -1] 
            l2 = float('-inf') if c2 == 0 else b[c2 -1] 
            r1 = float('inf') if c1 == n else a[c1] 
            r2 = float('inf') if c2 == m else b[c2] 
            
            if l1 <= r2 and l2 <= r1:
                return max(l1, l2)
            elif l1 >r2:
                h = c1 - 1
            else:
                l = c1 +1
        return -1



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while (T > 0):

        k = int(input())
        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.kthElement(a, b, k))
        print("~")
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
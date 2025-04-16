class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        #Your Code goes here.
        a , b = None , None
        C1, C2 = 0 , 0
        
        for n  in arr:
            if n == a:
                C1 += 1
            elif n == b:
                C2 += 1
            elif C1 ==0:
                a , C1 = n , 1
            elif C2 ==0:
                b, C2 = n , 1
            else:
                C1 -= 1
                C2 -= 1
        result = []
        n = len(arr)
        if a is not None and arr.count(a) > n // 3:
            result.append(a)
        if b is not None and b!= a and arr.count(b) > n // 3:
            result.append(b)
        return sorted(result)    

#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input().strip())
    for _ in range(t):
        s = input().strip()
        nums = list(map(int, s.split()))
        ob = Solution()
        ans = ob.findMajority(nums)
        if not ans:
            print("[]")
        else:
            print(" ".join(map(str, ans)))


if __name__ == "__main__":
    main()

# } Driver Code Ends
import math
class Solution:
    def mergeArrays(self, a, b):
        # code here
        n , m = len(a), len(b)
        gap = math.ceil(( n + m) / 2)
        while gap > 0:
            i, j = 0, gap
            while j < (n+ m):
                if i< n:
                    first = a[i]
                else:
                    first = b[i-n]
                if j< n:
                    second = a[j]
                else:
                    second = b[j-n]
                if first > second:
                    if i< n and j < n:
                        a[i], a[j] = a[j], a[i]
                    elif i< n:
                        a[i], b[j-n] = b[j - n], a[i]
                    else:
                        b[i -n], b[j-n] = b[j-n], b[i-n]
                i += 1
                j += 1
            gap = math.ceil(gap / 2) if gap > 1 else 0



#{ 
 # Driver Code Starts
# Input handling and main function
if __name__ == "__main__":
    # Number of test cases
    t = int(input().strip())

    for _ in range(t):
        # Input first array
        a = list(map(int, input().strip().split()))
        # Input second array
        b = list(map(int, input().strip().split()))

        # Create solution object and merge the arrays
        solution = Solution()
        solution.mergeArrays(a, b)

        # Output both arrays in the same line space-separated
        print(" ".join(map(str, a)))
        print(" ".join(map(str, b)))

        print("~")

# } Driver Code Ends
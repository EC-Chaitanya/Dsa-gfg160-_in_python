#User function Template for python3
class Solution:
	def twoSum(self, arr, target):
		# code here
		s = {}
		for i , n in enumerate(arr):
		    c = target - n
		    if c in s:
		        return True
		    s[n] = i
		return False


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Initial Template for Python 3


def main():
    T = int(input())
    while T > 0:
        x = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.twoSum(arr, x)
        if ans:
            print("true")
        else:
            print("false")
        T -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends

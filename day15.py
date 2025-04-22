# add two binary strings
#User function Template for python3
class Solution:
	def addBinary(self, s1, s2):
		# code here
         n1 = int(s1,2)
         n2 = int(s2,2)
         
         t = n1+ n2
         
         r = bin(t)[2:]
         return r
         

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        a = input().strip()
        b = input().strip()
        ob = Solution()
        answer = ob.addBinary(a, b)

        print(answer)
        print("~")

# } Driver Code Ends
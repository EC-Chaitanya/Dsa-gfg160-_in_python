class Solution:
    def minChar(self, s):
        #Write your code here
        n = len(s)
        rev = s[::-1]
        comb = s +'&' + rev
        lps = [0] * len(comb)
        for i in range(1, len(comb)):
            j = lps[i-1]
            while j > 0 and comb[i] != comb[j]:
                j = lps[j-1]
            if comb[i] == comb[j]:
                j += 1
            lps[i] = j
        return n - lps[-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        s = input()
        obj = Solution()
        ans = obj.minChar(s)
        print(ans)
        print("~")

# } Driver Code Ends
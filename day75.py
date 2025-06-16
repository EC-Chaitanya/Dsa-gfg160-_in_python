#User function Template for python3

class Solution:
    def findPermutation(self, s):
        def backtrack(path, used, res):
            if len(path) == len(s):
                res.append("".join(path))
                return
            for i in range(len(s)):
                if used[i]:
                    continue
                if i > 0 and s[i] == s[i-1] and not used[i-1]:
                    continue
                used[i] = True
                path.append(s[i])
                backtrack(path, used, res)
                path.pop()
                used[i] = False
        s = sorted(s)
        used= [False]* len(s)
        result = []
        backtrack([], used, result)
        return result
        

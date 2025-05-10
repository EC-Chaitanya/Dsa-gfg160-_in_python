class Solution:
    # Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self, mat):
        # code here
        r = []
        if not mat:
            return r
        t , b = 0, len(mat) -1
        left, right = 0 , len(mat[0]) - 1
        while t <= b and left<= right:
            for i in range(left, right+1):
                r.append(mat[t][i])
            t += 1
            for i in range (t, b+1):
                r.append(mat[i][right])
            right -= 1
            if t<= b:
                for i in range(right, left-1 , -1):
                    r.append(mat[b][i])
                b -= 1
            if left <= right:
                for i in range(b, t -1, -1):
                    r.append(mat[i][left])
                left +=1
        return r
            


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()

    t = int(data[0])
    index = 1
    for _ in range(t):
        r = int(data[index])
        c = int(data[index + 1])
        index += 2
        matrix = []
        for i in range(r):
            row = list(map(int, data[index:index + c]))
            matrix.append(row)
            index += c

        solution = Solution()
        result = solution.spirallyTraverse(matrix)
        print(" ".join(map(str, result)))
        print("~")

# } Driver Code Ends
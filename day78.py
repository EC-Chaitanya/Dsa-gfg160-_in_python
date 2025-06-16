#User function Template for python3

class Solution:
    
    #Function to find a solved Sudoku. 
    def solveSudoku(self, mat):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty = []
        for i in range(9):
            for j in range(9):
                num = mat[i][j]
                if num == 0:
                    empty.append((i, j))
                else:
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes(i // 3)* 3 + (j// 3)
    def backtrack(idx):
        if idx == len(empty):
            return True
        i, j = empty[idx]
        boxId = ( i//3 )* 3 + (j//3)
        for num in range(1, 10):
            if num not in rows[i]and num not in cols[j] and num not in boxes:
                mat[i][j] = num
                rows[i].add(num)
                cols[j].add(num)
                boxes[boxId].add(num)
                if backtrack(idx + 1):
                    return True
                mat[i][j] = 0
                rows[i]. remove(num)
                cols[j].remove(num)
                boxes[boxId].remove(num)
        return False
    backtrack(0)
        

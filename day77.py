def solveNQueens(n):
    def backtrack(col, queens, rows, diagonals1, diagonals2):
        if col == n:
            result.append(queens[:])
            return
        
        for row in range(1, n + 1):
            if row in rows or (row - col) in diagonals1 or (row + col) in diagonals2:
                continue
            
            queens.append(row)
            rows.add(row)
            diagonals1.add(row - col)
            diagonals2.add(row + col)
            
            backtrack(col + 1, queens, rows, diagonals1, diagonals2)
            
            # backtrack
            queens.pop()
            rows.remove(row)
            diagonals1.remove(row - col)
            diagonals2.remove(row + col)
    
    result = []
    backtrack(0, [], set(), set(), set())
    return result

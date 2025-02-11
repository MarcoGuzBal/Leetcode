class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        column = set()
        square = set()

        for i in range(len(board)):
            row = set()
            for num in board[i]:
                if num in row:
                    return False
                elif num != '.':
                    row.add(num)

        for i in range(len(board)):
            column = set()
            for j in range(len(board)):
                currNum = board[j][i]
                if currNum in column:
                    return False
                elif currNum != '.':
                    column.add(currNum)

        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    
                    if board[row][col] in seen:
                        return False
                    elif board[row][col] != '.':
                        seen.add(board[row][col])
            
        return True

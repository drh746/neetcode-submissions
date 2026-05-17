class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in range(9):
            hash_row = set()
            for col in range(9):
                if board[row][col] == ".":
                    continue
                if board[row][col] not in hash_row:
                    hash_row.add(board[row][col]) 
                else:
                    return False

        for col in range(9):
            hash_col = set()
            for row in range(9):
                if board[row][col] == ".":
                    continue
                if board[row][col] not in hash_col:
                    hash_col.add(board[row][col]) 
                else:
                    return False
        
        for square in range(9):
            hash_square = set()
            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] not in hash_square:
                        hash_square.add(board[row][col]) 
                    else:
                        return False
        return True

        
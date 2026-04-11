class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col = collections.defaultdict(set)
        rol = collections.defaultdict(set)
        square = collections.defaultdict(set)
        for c in range(9):
            for r in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in col[c] or
                    board[r][c] in rol[r] or
                    board[r][c] in square[(r//3, c//3)]):
                    return False
                col[c].add(board[r][c])
                rol[r].add(board[r][c])
                square[(r//3, c//3)].add(board[r][c])
                
        return True

        
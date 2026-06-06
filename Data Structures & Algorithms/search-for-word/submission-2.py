class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        row = len(board)
        col = len(board[0])

        def build(idx, y, x):
            if idx == len(word):
                return True
            if y<0 or y>row-1 or x<0 or x>col-1:
                return False
            if (y,x) in path:
                return False
            
            if board[y][x] == word[idx]:
                path.add((y,x))
                for dy, dx in direction:
                    if build(idx+1, y+dy, x+dx):
                        return True
                path.remove((y,x))

            return False
        
        path = set()
        direction = [(1,0), (0,1), (-1,0), (0,-1)]

        for i in range(row):
            for j in range(col):
                if build(0,i,j):
                    return True
        
        return False




        
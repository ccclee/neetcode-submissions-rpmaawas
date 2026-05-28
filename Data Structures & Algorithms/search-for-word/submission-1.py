class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])
        visited = [[0 for _ in range(col)] for _ in range(row)]

        direction = [[0,1],[1,0],[-1,0],[0,-1]]

        def possible (a,b,i):
            nonlocal visited
            if i == len(word)-1:
                return True
            elif i > len(word)-1:
                return False
            for dx, dy in direction:
                if 0<=a+dx<col and 0<=b+dy<row and not visited[b+dy][a+dx]:
                    if board[b+dy][a+dx] == word[i+1]:
                        visited[b+dy][a+dx] =1
                        if possible (a+dx,b+dy,i+1):
                            return True
                        visited[b+dy][a+dx] =0
        
        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0]:
                    visited[i][j]=1
                    if possible (j,i,0):
                        return True
                    visited[i][j]=0
        

        return False



        
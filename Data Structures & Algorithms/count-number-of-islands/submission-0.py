class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        visited =[[0 for _ in range(col)]for _ in range(row)]

        def unconnected(i,j):
            if i+1 < row and grid[i+1][j]== "1" and not visited[i+1][j]:
                visited[i+1][j] = 1
                grid[i+1][j] = "0"
                unconnected(i+1,j)
            if i-1 >= 0 and grid[i-1][j]== "1" and not visited[i-1][j]:
                visited[i-1][j] = 1
                grid[i-1][j] = "0"
                unconnected(i-1,j)
            if j+1 < col and grid[i][j+1]== "1" and not visited[i][j+1]:
                visited[i][j+1] = 1
                grid[i][j+1] = "0"
                unconnected(i,j+1)
            if j-1 >= 0 and grid[i][j-1]== "1" and not visited[i][j-1]:
                visited[i][j-1] = 1
                grid[i][j-1] = "0"
                unconnected(i,j-1)
        
        for i in range(row):
            for j in range(col):
                if not visited[i][j]:
                    visited[i][j] = 1
                    if grid[i][j]=="1":
                        unconnected(i,j)
        
        count = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j]=="1":
                    count +=1

        return count
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        pacific = set()
        atlantic = set()
        direction = [[0,1],[1,0],[-1,0],[0,-1]]
        row = len(heights)
        col = len(heights[0])

        def fromPacific(r,c):
            pacific.add((r,c))
            for dr, dc in direction:
                if 0<=r+dr<row and 0<=c+dc<col and (r+dr, c+dc) not in pacific and heights[r+dr][c+dc] >= heights[r][c] :
                    fromPacific(r+dr,c+dc)
        def fromAtlantic(r,c):
            atlantic.add((r,c))
            for dr, dc in direction:
                if 0<=r+dr<row and 0<=c+dc<col and (r+dr, c+dc) not in atlantic and heights[r+dr][c+dc] >= heights[r][c] :
                    fromAtlantic(r+dr,c+dc)

        for i in range(col):
            fromPacific(0,i)
            fromAtlantic(row-1,i)
        for j in range(row):
            fromPacific(j,0)
            fromAtlantic(j,col-1)
        
        res = []
        for n in pacific:
            if n in atlantic:
                res.append([n[0],n[1]])
        return res
        

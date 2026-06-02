class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res = 1
        for i in range(m+n-2,m-1,-1):
            res*=i
        for i in range(n-1,0,-1):
            res/=i
        
        return int(res)
        
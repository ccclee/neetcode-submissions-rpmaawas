class Solution:
    def countSubstrings(self, s: str) -> int:

        n = len(s)
        res = 0
        def expand(i,j):
            while i>=0 and j<n and s[i]==s[j]:
                i-=1
                j+=1
            length = (j-1)-(i+1)+1
            return math.ceil(length/2)
        
        for i in range(n):
            res += expand(i,i) + expand(i,i+1)
        
        return res
        
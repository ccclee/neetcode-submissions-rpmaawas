class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        def expand(a, b):
            
            if a<0 or b>n-1:
                return [a+1,b-1]
            if s[a]!=s[b]:
                return [a+1,b-1]
            return expand(a-1, b+1)

        start, end = 0,0
        for i in range(n):
            a,b = expand(i,i)
            if (b-a)> (end-start):
                start, end = a, b 
            c, d = expand(i,i+1)
            if (d-c)> (end-start):
                start, end = c, d

        return s[start:end+1]


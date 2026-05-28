class Solution:
    def longestPalindrome(self, s: str) -> str:

        n = len(s)
        res =""

        def expand(i,j):
            while(i>=0 and j<n and s[i]==s[j]):
                i-=1
                j+=1
            return s[i+1:j]

        for i in range(n):
            left = expand(i,i)
            right = expand(i,i+1)

            if len(left)>len(res):
                res = left
            if len(right)>len(res):
                res = right
        
        return res
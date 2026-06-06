class Solution:
    def numDecodings(self, s: str) -> int:
        if int(s[0]) == 0:
            return 0
        memo = [0 for _ in range(len(s)+1)]
        memo[0], memo[1] = 1,1
        for i in range(1,len(s)):
            acc =0
            if 10<= int(s[i-1:i+1])<=26:
                acc += memo[i-1]
            if int(s[i])>0:
                acc+=memo[i]
            memo[i+1] = acc
        return memo[len(s)]

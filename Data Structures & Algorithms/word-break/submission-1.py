class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        words = set(wordDict)
        memo = {}

        def helper(string):
            if not string :
                return True
            if string in memo:
                return memo[string]
            for i in range(1,len(string)+1):
                if string[:i] in words and helper(string[i:]):
                    memo[string] = True
                    return True
                
            memo[string] =False
            return False
        return helper(s)
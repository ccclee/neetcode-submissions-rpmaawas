class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sdic, tdic= {}, {}
        for i in range(len(s)):
            sdic[s[i]] = sdic.get(s[i], 0) +1
            tdic[t[i]] = tdic.get(t[i], 0) +1
        return sdic == tdic
        
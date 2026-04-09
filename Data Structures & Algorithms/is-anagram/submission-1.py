class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        s_char = {}
        t_char = {}
        for c in range(len(s)):
            s_char[s[c]] = s_char.get(s[c], 0) + 1
            t_char[t[c]] = t_char.get(t[c], 0) + 1
        return s_char == t_char
        


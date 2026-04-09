class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_char = {}
        t_char = {}
        for c in range(len(s)):
            char = s[c]
            s_char[char] = s_char.get(char, 0) + 1
        for c in range(len(t)):
            char = t[c]
            t_char[char] = t_char.get(char, 0) + 1
        return s_char == t_char
        


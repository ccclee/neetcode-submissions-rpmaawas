class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        s1c = [0] * 26
        s2c = [0] * 26
        for s in s1:
            s1c[ord(s) - ord('a')]+=1
        for i in range(len(s1)):
            s2c[ord(s2[i]) - ord('a')]+=1
        if s1c == s2c:
            return True
        
        l= 0
        for r in range(len(s1), len(s2)):
            s2c[ord(s2[l]) - ord('a')]-=1
            s2c[ord(s2[r]) - ord('a')]+=1
            if s1c == s2c:
                return True
            l+=1
        return False
        


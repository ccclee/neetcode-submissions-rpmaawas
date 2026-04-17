class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        s1count = [0] * 26
        for s in s1:
            s1count[ord(s)-ord('a')] += 1
        l = 0
        r = len(s1) - 1
        while r < len(s2):
            s2count = [0] * 26
            for i in range(l ,r+1):
                s2count[ord(s2[i])-ord('a')] += 1
            if s1count == s2count:
                return True
            l+=1
            r+=1
        return False
            

        
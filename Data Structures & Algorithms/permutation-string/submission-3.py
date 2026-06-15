class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        target = {}
        window ={}
        for i in range(len(s1)):
            target[s1[i]] = target.get(s1[i],0)+1
            window[s2[i]] = window.get(s2[i],0)+1
        if window == target:
                return True

        for r in range(len(s1),len(s2)):
            window[s2[r]] = window.get(s2[r],0)+1
            window[s2[r-len(s1)]]-=1
            if window[s2[r-len(s1)]]== 0:
                del window[s2[r-len(s1)]]
            if window == target:
                return True
        return False

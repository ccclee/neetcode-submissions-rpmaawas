class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)< len(t):
            return ""

        mapt = Counter(t)
        res = ""
        minL = float("inf")

        need = len(mapt)
        have = 0
        
        l = 0
        window = {}

        for r in range(len(s)):
            if s[r] in mapt:
                window[s[r]] = window.get(s[r],0)+1
                if window[s[r]] == mapt[s[r]]:
                    have+=1

            while have == need:
                if minL > r-l+1:
                    res = s[l:r+1]
                    minL = r-l+1
                if s[l] in mapt:
                    window[s[l]]-=1
                    if window[s[l]] < mapt[s[l]]:
                        have-=1
                l+=1
        return res
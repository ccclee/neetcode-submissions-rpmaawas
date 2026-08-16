class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        curr = []

        def palindrome(s):
            for i in range(len(s)//2):
                if s[i]!=s[len(s)-1-i]:
                    return False
            return True

        def helper(i):
            if i == len(s):
                res.append(curr.copy())
                return

            for j in range(i, len(s)):
                substring = s[i:j+1]

                if not palindrome(substring):
                    continue

                curr.append(substring)

                helper(j+1)

                curr.pop()

        helper(0)
        return res
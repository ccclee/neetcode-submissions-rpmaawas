class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        res = 0
        for num in numset:
            if num+1 not in numset:
                l = 1
                curr = num
                while (curr-1) in numset:
                    l+=1
                    curr = curr-1
                res = max(res,l)
        return res
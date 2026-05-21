class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = len(nums)
        res = l
        for i in range(l):
            res ^= nums[i]
            res ^= i
        return res

        
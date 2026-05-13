class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        currmax = nums[0]
        for n in nums[1:]:
            currmax = max(currmax+n, n)
            res = max(res,currmax)

        return res
        
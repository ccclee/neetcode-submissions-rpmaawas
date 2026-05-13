class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currmax = nums[0]
        res = currmax
        for n in nums[1:]:
            currmax = max(currmax+n, n)
            res = max(res,currmax )

        return res
        
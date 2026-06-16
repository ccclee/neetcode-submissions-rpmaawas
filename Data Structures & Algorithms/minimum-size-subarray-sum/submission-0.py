class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        minLength = float("inf")
        l = 0
        currsum = 0
        for r in range(len(nums)):
            currsum += nums[r]
            while currsum - nums[l] >= target:
                currsum -= nums[l]
                l+=1
            if currsum>=target:
                minLength = min(minLength, r-l+1)
        if minLength == float("inf"):
            return 0
        return minLength


        
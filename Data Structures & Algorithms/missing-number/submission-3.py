class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = len(nums)
        expectsum = (1+l)*l//2
        return expectsum - sum(nums)
        
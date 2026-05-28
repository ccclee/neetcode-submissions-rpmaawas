class Solution:
    def rob(self, nums: List[int]) -> int:
        size = len(nums)
        if size ==1:
            return nums[0]
        if size ==2:
            return max(nums[0],nums[1])

        acc = [0 for _ in range(size)]
        acc[0] = nums[0]
        acc[1] = max(nums[0],nums[1])

        for i in range(2,size):
            acc[i] = max(acc[i-1], nums[i]+acc[i-2])

        return acc[-1]

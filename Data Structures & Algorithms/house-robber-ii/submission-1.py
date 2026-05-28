class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]

        def rob_sub(arr):
            prev2 = 0
            prev1 = 0

            for money in arr:
                current = max(prev2+money, prev1)
                prev2 = prev1
                prev1 = current
            
            return prev1
        
        return max(rob_sub(nums[:-1]), rob_sub(nums[1:]))
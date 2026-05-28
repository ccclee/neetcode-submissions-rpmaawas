class Solution:
    def rob(self, nums: List[int]) -> int:
        size =len(nums)

        if size == 1:
            return nums[0]
        elif size == 2:
            return max(nums[0], nums[1])
        elif size == 3:
            return max(nums[0], nums[1], nums[2])

        acc1 = [0 for _ in range(size-1)] 
        acc2 = [0 for _ in range(size-1)] 

        acc1[0] = nums[0]
        acc1[1] = max(nums[0], nums[1])
        for i in range(2,size-1):
            acc1[i] = max(acc1[i-1], nums[i]+ acc1[i-2])

        acc2[0] = nums[1]
        acc2[1] = max(nums[1], nums[2])
        for i in range(2,size-1):
            acc2[i] = max(acc2[i-1], nums[i+1]+ acc2[i-2])

        return max(acc1[-1], acc2[-1])

        
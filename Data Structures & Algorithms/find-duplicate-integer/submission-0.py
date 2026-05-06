class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            k = abs(nums[i])
            if nums[k]<0:
                return k
            else :
                nums[k]*=(-1)

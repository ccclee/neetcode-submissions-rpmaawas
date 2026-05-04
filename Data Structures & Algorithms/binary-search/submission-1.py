class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0 
        j = len(nums) -1
        while j>=i:
            mid = (j-i)//2 + i
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                i = mid+1
            else:
                j = mid-1
        return -1


        
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        preMap = {}
        for index, num in enumerate(nums):
            diff = target - num
            if diff in preMap:
                return [preMap[diff], index]
            preMap[num] = index
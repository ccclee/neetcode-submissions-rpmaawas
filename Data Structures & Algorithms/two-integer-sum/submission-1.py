class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        beforeMap = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in beforeMap:
                return [beforeMap[diff], i]
            beforeMap[nums[i]] = i

        
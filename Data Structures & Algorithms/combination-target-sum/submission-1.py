class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        def combine(start, left, curr):
            if left == 0:
                res.append(curr)
            else:
                for i in range(start, len(nums)):
                    if nums[i] <= left:
                        combine(i,left - nums[i], curr+[nums[i]])

        res = []

        combine(0,target,[])

        return res
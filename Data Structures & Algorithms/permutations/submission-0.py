class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)

        def helper(i):
            if i ==n:
                res.append(nums[:])

            for j in range(i,n):
                nums[i], nums[j] = nums[j], nums[i]
                helper(i+1)
                nums[i], nums[j] = nums[j], nums[i]
        res = []
        helper(0)

        return res
        
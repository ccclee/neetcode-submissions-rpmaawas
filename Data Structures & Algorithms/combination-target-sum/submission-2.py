class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res =[]
        length = len(nums)

        def helper (curr, left, idx):
            nonlocal res
            if left==0:
                res.append(curr)
                return 
            for i in range(idx,length):
                if nums[i] <= left:
                    helper (curr+ [nums[i]], left - nums[i], i)
        
        helper ([], target, 0)

        return res
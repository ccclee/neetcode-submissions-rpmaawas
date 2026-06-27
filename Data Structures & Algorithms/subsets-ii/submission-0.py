class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res =[]
        curr =[]
        nums.sort()
        length = len(nums)

        def helper(idx):
            res.append(curr.copy())

            for i in range(idx, length):
                if i > idx and nums[i] == nums[i - 1]:
                    continue

                curr.append(nums[i])
                helper(i + 1)
                curr.pop()

        helper(0)
        
        return res
        
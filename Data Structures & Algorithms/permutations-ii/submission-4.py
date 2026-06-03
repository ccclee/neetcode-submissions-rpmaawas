class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
      
        def build(i):
            if i == len(nums):
                res.append(nums[:])
            used = set()
            for j in range(i,len(nums)):
                if nums[j] in used:
                    continue
                used.add(nums[j])
                nums[i], nums[j] = nums[j], nums[i]
                build(i+1)
                nums[i], nums[j] = nums[j], nums[i]

        res = []
        build(0)
        return res

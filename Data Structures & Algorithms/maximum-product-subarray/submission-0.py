class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pairs=[]
      
        currmax = nums[0]
        currmin = nums[0]
        pairs.append((currmax,currmin))

        overallmax = currmax
        overallmin = currmin

        for i in range(1,len(nums)):
            currmax = max(nums[i], nums[i]*pairs[i-1][0],nums[i]*pairs[i-1][1])
            currmin = min(nums[i], nums[i]*pairs[i-1][0],nums[i]*pairs[i-1][1])
            pairs.append((currmax,currmin))

            overallmax = max(overallmax, currmax)
            overallmin = min(overallmin, currmin)

        return overallmax
        
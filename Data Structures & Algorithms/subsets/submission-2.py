class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        def build(i,ans):
            if i == n:
                res.append(ans)
                return 
            build(i+1,ans)
            build(i+1,ans+[nums[i]])
            

        res =[]
        build(0,[])
        return res

        
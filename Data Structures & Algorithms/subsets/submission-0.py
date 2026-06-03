class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        def build(i,ans):
            nonlocal res
            if i == n:
                res.append(ans[:])
                return 

            build(i+1, ans)

            ans.append(nums[i])
            build(i+1, ans)
            ans.pop()

        res =[]
        build(0,[])
        return res

        
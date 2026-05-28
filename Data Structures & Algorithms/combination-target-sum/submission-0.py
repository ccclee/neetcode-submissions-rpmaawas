class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []

        def combine(comb, left, choose):
            if left ==0:
                nonlocal res
                res.append(comb)

            else:
                for i in range(len(choose)):
                    if choose[i]<= left:
                        combine(comb+[choose[i]], left-choose[i], choose[i:])
                        
        combine([], target, nums)

        return res
        
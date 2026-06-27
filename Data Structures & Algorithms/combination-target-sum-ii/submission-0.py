class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        lenght = len(candidates)

        def helper(curr, left, idx):
            if left == 0:
                res.append(curr)
                return
            prev = 0
            for i in range(idx,lenght):
                if prev != candidates[i] and candidates[i]<=left:
                    helper(curr + [candidates[i]], left -candidates[i], i+1)
                    prev = candidates[i]
        
        helper([], target, 0)

        return res
                    

        
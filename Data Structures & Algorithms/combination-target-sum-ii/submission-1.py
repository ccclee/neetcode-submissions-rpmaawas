class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        lenght = len(candidates)
        curr =[]

        def helper(left, idx):
            nonlocal curr
            if left == 0:
                res.append(curr[:])
                return
            prev = 0
            for i in range(idx,lenght):
                if i > idx and candidates[i-1]== candidates[i]:
                    continue
                if  candidates[i]>left:
                    break
                curr.append(candidates[i])
                helper(left -candidates[i], i+1)
                curr.pop()
    
        helper(target, 0)

        return res
                    

        
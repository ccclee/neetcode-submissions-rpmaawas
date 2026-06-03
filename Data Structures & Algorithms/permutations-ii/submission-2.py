class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        n = len(nums)
        def dfs(ans, visited):
            if len(ans) == n:
                res.append(ans[:])
            prev = None
            for i in range(n):
                if i in visited:
                    continue
                if prev == nums[i]:
                    continue

                prev = nums[i]

                visited.add(i)
                ans.append(nums[i])

                dfs(ans,visited)

                visited.remove(i)
                ans.pop()

        res = []
        visited = set()
        dfs([],visited)

        return res

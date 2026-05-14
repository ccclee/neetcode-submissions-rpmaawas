class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        appear = set()
        for n in nums:
            if n in appear:
                return n
            appear.add(n)
        
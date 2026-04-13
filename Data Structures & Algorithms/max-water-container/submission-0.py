class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        maxvol = 0
        while j > i:
            currentvol = (j - i) * min( heights[i], heights[j])
            maxvol = max(currentvol, maxvol)
            if heights[i] >= heights[j]:
                j -= 1
            else:
                i += 1
        return maxvol

        
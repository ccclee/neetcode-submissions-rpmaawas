class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) -1 
        maxvolume = 0 
        while j > i:
            curvolume = min(heights[i], heights[j]) * (j-i)
            maxvolume = max(maxvolume, curvolume)
            if heights[j] <= heights[i]:
                j-=1
            else:
                i+=1
        return maxvolume


        
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort()
        res = -1
        prevstart, prevend = intervals[0]
        for start, end in intervals:
            if prevend <= start:
                prevstart, prevend = start, end
            else:
                res+=1
                prevend = min(prevend,end) 

        return res
        
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        l = len(intervals)
        if l ==1:
            return 0
        res =[]
        res.append(intervals[0])
        for i in range(1, l):
            if res[-1][1] <= intervals[i][0]:
                res.append(intervals[i])
            elif res[-1][1] > intervals[i][1]:
                res[-1]=intervals[i]
        
        return l - len(res)
        
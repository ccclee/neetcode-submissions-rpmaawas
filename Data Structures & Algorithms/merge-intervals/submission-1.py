class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key = lambda x: x[0])
        res =[]
        currstart, currend = intervals[0]
        for i in range(1, len(intervals)):
            if currend < intervals[i][0]:
                res.append([currstart,currend])
                currstart,currend = intervals[i]
                i += 1
            else:
                currstart = min(currstart, intervals[i][0])
                currend = max(currend, intervals[i][1])
                i += 1
        res.append([currstart,currend])

        return res
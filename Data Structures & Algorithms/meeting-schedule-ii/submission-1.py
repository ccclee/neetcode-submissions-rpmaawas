"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key = lambda x:x.start)
        heap = []
        heapq.heappush(heap,0)
        for i in intervals:
            earliestend = heapq.heappop(heap)
            if i.start< earliestend:
                heapq.heappush(heap,earliestend)
                heapq.heappush(heap,i.end)
            else:
                heapq.heappush(heap,i.end)

        return len(heap)




        
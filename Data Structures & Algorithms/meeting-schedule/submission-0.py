"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        heap = []
        for interval in intervals:
            start = interval.start
            end = interval.end
            heapq.heappush(heap, (start,end))

        if heap:
            firststart, firstend = heapq.heappop(heap)


        while heap:
            secondstart, secondend = heapq.heappop(heap)
            if firstend > secondstart:
                return False
            firststart, firstend = secondstart, secondend

        return True

            




"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) < 2:
            return True
        
        intervals.sort(key=lambda x: x.start)

        i = 1
        while i < len(intervals):
            #if it starts before the last one ends
            if intervals[i].start < intervals[i-1].end:
                return False
            i += 1
        return True

        
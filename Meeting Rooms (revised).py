"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # Start with sort
        intervals.sort(key = lambda interval : interval.start)

        # Can start at index 1 because index 0 has nothing to compare with
        for i in range(1, len(intervals)):
            curr_start = intervals[i].start
            prev_end = intervals[i-1].end
            if curr_start < prev_end:
                return False
        return True
            
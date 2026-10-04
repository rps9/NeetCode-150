"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        valid_intervals = []
        for interval in intervals: 
            for valid_interval in valid_intervals:
                if interval.start >= valid_interval.start and interval.start < valid_interval.end:
                    return False
            valid_intervals.append(interval)
        return True
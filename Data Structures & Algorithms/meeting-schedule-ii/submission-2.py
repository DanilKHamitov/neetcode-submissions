"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted([x.start for x in intervals])
        end  = sorted([x.end for x in intervals])
        count = 0
        s = e = 0
        res = 0
        while s<len(intervals):
            if starts[s] < end[e]:
                s += 1
                count +=1
            else:
                count -=1
                e +=1
            res = max(count,res)
        return res
                

        
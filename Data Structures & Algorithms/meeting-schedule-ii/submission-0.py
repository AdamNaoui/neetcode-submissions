"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq as hp

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        queue=[]
        next_day_queue=[]
        for interval in intervals:
            hp.heappush(next_day_queue,(interval.start,interval.end))
        
        res=0
        while queue or next_day_queue:
            print(queue,next_day_queue)
            if not queue:
                queue=next_day_queue
                res+=1
                next_day_queue=[]
            start,end=hp.heappop(queue)
            while queue and queue[0][0]<end:
                hp.heappush(next_day_queue,hp.heappop(queue))
            

        return res

        
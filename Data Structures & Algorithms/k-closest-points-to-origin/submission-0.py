import heapq as hp
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap=[]

        for [x,y] in points:
            dist=math.sqrt(x*x+y*y)
            hp.heappush(min_heap,(dist,[x,y]))
        
        res=[]

        for i in range(k):
            _,point=hp.heappop(min_heap)
            res.append(point)

        return res


        
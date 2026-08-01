import heapq as hp

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        sorted_intervals=[]

        for [left,right] in intervals:
            hp.heappush(sorted_intervals,(left,right))
        
        res=[]

        for query in queries:
            trash=[]

            while sorted_intervals and sorted_intervals[0][1]<query:
                trash.append(hp.heappop(sorted_intervals))
            
            best=-1
            
            while sorted_intervals and sorted_intervals[0][0]<=query:
                left,right=hp.heappop(sorted_intervals)
                trash.append((left,right))
                if right>=query:
                    best= right-left+1 if best==-1 else min(best,right-left+1)

            res.append(best)

            for interval in trash:
                hp.heappush(sorted_intervals,interval)
            
        
        return res

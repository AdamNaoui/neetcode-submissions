import heapq as hp

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        queue=[]

        for [st,end] in intervals:
            hp.heappush(queue,(st,end))
        
        res=[]

        while queue:
            st,end=hp.heappop(queue)

            while queue and (st<=queue[0][1]<=end or st<=queue[0][0]<=end ):
                new_st,new_end=hp.heappop(queue)
                st=min(st,new_st)
                end=max(end,new_end)
            
            res.append([st,end])
        
        return res
        
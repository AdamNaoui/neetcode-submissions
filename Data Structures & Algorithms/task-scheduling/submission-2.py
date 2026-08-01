import heapq as hp

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter={}

        for task in tasks:
            if task not in counter:
                counter[task]=0
            
            counter[task]+=1
        

        p_queue=[]

        for task,count in counter.items():
            hp.heappush(p_queue,(0,-count,task))
        

        curr_cycle=0
    
        while p_queue:
            while p_queue and p_queue[0][0]<curr_cycle:
                index,neg_count,task=hp.heappop(p_queue)
                hp.heappush(p_queue,(curr_cycle,neg_count,task))

            index,neg_count,task=hp.heappop(p_queue)
            curr_cycle=max(index,curr_cycle)
            
            curr_cycle+=1
            neg_count+=1

            if neg_count==0:
                continue
            
            hp.heappush(p_queue,(curr_cycle+n,neg_count,task))
        
        return curr_cycle








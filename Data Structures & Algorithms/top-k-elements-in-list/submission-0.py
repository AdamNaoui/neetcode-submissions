class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_freq={}
        buckets={}
        max_freq=0
        for num in nums:
            if num not in nums_freq:
                nums_freq[num]=0
            nums_freq[num]+=1
            freq=nums_freq[num]
            max_freq=max(max_freq,freq)
            if freq not in buckets:
                buckets[freq]=set()
            
            buckets[freq].add(num)
            if freq-1 in buckets and num in buckets[freq-1]:
                buckets[freq-1].remove(num)

        i=0 
        res=[]
    
        for freq in range(max_freq,-1,-1):
            if i>=k:
                return res
            if freq not in buckets:
                continue
            
            res+=list(buckets[freq])
            i+=len(buckets[freq])
        return res



            
            


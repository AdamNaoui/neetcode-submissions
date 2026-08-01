class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res=[]

        bigger_interval=[num for num in newInterval]
        is_added=False
        for interval in intervals:
            if interval[1]<newInterval[0]:
                res.append(interval)
                continue
            
            if interval[0]>newInterval[1]:
                if not is_added:
                    is_added=True
                    res.append([num for num in bigger_interval])
                
                res.append(interval)
            
            bigger_interval[0]=min(bigger_interval[0],interval[0])
            bigger_interval[1]=max(bigger_interval[1],interval[1])
        
        if not is_added:
            res.append([num for num in bigger_interval])
        
        return res
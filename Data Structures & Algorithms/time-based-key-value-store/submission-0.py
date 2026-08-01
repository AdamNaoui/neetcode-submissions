class TimeMap:

    def __init__(self):
        self.vals={}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.vals:
            self.vals[key]=[]
        
        self.vals[key].append((timestamp,value))
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.vals:
            return ""
        
        timestamps_and_vals=self.vals[key]
        l,r=0,len(timestamps_and_vals)-1

        res=""
        while l<=r:
            mid=l+(r-l)//2
            curr_t,curr_value=timestamps_and_vals[mid]
            if curr_t==timestamp:
                return curr_value
            
            if curr_t<timestamp:
                res=curr_value
                l=mid+1
                continue
            r=mid-1
        return res

       
        

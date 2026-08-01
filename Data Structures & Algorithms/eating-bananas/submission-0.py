class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_rate=max(piles)

        low,high=1,max_rate
        res=max_rate
        while low<=high:
            mid=low+(high-low)//2

            total=0
            for pile in piles:
                total+=pile//mid if pile % mid==0 else pile//mid+1
                if total>h:
                    break
            
            if total>h:
                low=mid+1
                continue
            
            res=mid
            high=mid-1
        
        return res

        
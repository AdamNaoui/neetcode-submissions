class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1

        while l<=r:
            mid=l+(r-l)//2
            mid_num=nums[mid]

            if mid_num==target:
                return mid
            
            if mid_num<target:
                l=mid+1
                continue
            
            r=mid-1
        
        return -1
            
        
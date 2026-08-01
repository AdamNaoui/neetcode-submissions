class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1

        while l<=r:
            mid=l+(r-l)//2
            print(l,mid,r)
            if nums[mid]==target:
                return mid
            
            if target<nums[mid]:
                if target<nums[l] and nums[mid]>=nums[l]:
                    l=mid+1
                    continue
                
             
                r=mid-1
                continue
            
            if target > nums[r] and nums[mid]<=nums[r]:
                r=mid-1
                continue
            l=mid+1

        return -1
        
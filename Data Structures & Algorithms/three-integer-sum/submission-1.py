class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        res=[]

        cache=set()

        for i,pivot in enumerate(nums):
            target=-pivot

            left=i+1
            right=len(nums)-1

            while left<right:
                if nums[left]+nums[right]==target:
                    solution=[pivot,nums[left],nums[right]]
                    solution.sort()
                    key="".join(str(num) for num in solution)
                    if key not in cache:
                        res.append(solution)
                        cache.add(key)
                    left+=1
                    continue
                
                if nums[left]+nums[right]>target:
                    right-=1
                    continue
                
                left+=1
        
        return res
        

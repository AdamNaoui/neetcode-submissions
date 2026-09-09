class Solution:
    def rob(self, nums: List[int]) -> int:
        cache={}
        def helper(house,robbed_first):
            if house == len(nums)-1:
                return nums[house] if not robbed_first else 0
            
            if house >=len(nums):
                return 0
            
            if (house,robbed_first) in cache:
                return cache[(house,robbed_first)]
            
            robbed=helper(house+2,True) if house == 0 else helper(house+2,robbed_first)
            robbed+=nums[house]

            not_robbed=helper(house+1,robbed_first)

            best=max(robbed,not_robbed)

            cache[(house,robbed_first)]=best
            return best
        
        return helper(0,False)

        
class Solution:
    def rob(self, nums: List[int]) -> int:
        cache={}
        def helper(house):
            if house>=len(nums):
                return 0
            
            if house in cache:
                return cache[house]
            
            best = max(nums[house]+helper(house+2),helper(house+1))
            cache[house]=best
            return best
        
        return helper(0)

        
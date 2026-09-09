class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache={}

        def helper(stair):
            if stair>=len(cost):
                return 0
            
            if stair in cache:
                return cache[stair]
            
            best=cost[stair]+ min(helper(stair+1),helper(stair+2))
            cache[stair]=best
            return best
        
        return min(helper(0),helper(1))
        
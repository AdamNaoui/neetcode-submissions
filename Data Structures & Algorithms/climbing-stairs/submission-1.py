class Solution:
    def climbStairs(self, n: int) -> int:
        memo={}
        def helper(stair):
            if stair in memo:
                return memo[stair]
            if stair == n:
                return 1
            if stair > n:
                return 0
            
            memo[stair]=helper(stair+1)+helper(stair+2)
            return  memo[stair]
        return helper(0)
        
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        cache={}
        def helper(idx, m, is_alice):
            if (idx, m, is_alice) in cache:
                return cache[(idx, m, is_alice)]
            
            if idx >= len(piles):
                return 0
            
            best_a = 0
            best_b = float("inf")

            gain = 0
            for x in range(1, 2*m + 1):
                if idx + x - 1 >= len(piles):
                    break
                
                gain += piles[idx + x - 1]
                nxt_m = max(m, x)
                
                if is_alice:
                    res = gain + helper(idx + x, nxt_m, False)
                    best_a = max(best_a, res)
                else:
                    res = helper(idx + x, nxt_m, True)
                    best_b = min(best_b, res)
            
            best = best_a if is_alice else best_b
            cache[(idx, m, is_alice)] = best
            return best

        return helper(0, 1, True)
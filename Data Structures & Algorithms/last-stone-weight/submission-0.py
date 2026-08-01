import heapq as hp

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        queue=[] # max heap

        for stone in stones:
            hp.heappush(queue,-stone)
        
        while len(queue)>1:
            stone_1,stone_2=-hp.heappop(queue),-hp.heappop(queue)

            if stone_1==stone_2:
                continue
            
            new_stone=stone_1-stone_2
            hp.heappush(queue,-new_stone)
        
        return 0 if not queue else -queue[0]
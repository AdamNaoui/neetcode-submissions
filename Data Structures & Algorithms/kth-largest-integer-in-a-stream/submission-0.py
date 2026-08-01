import heapq as hp
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.queue=[]
        
        for num in nums:
            hp.heappush(self.queue,-num)
        

    def add(self, val: int) -> int:
        hp.heappush(self.queue,-val)

        pool=[]

        for i in range(self.k):
            pool.append((hp.heappop(self.queue)))
        
        res=-pool[-1]

        while pool:
            hp.heappush(self.queue,pool.pop())

        return res
        

import heapq as hp

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap=[]

        for num in nums:
            hp.heappush(max_heap,-num)
        
        for i in range(k-1):
            hp.heappop(max_heap)
        
        return -hp.heappop(max_heap)
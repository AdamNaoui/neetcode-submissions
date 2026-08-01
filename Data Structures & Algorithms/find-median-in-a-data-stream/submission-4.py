import heapq as hp
class MedianFinder:

    # split the sorted stream in two half (left part as max heap and right aprt as min heap)
    def __init__(self):
        self.left_max_heap=[]
        self.right_min_heap=[]

    def addNum(self, num: int) -> None:
        hp.heappush(self.left_max_heap,-num)
        if len(self.left_max_heap)>len(self.right_min_heap)+1:
            num_to_move=-(hp.heappop(self.left_max_heap))
            hp.heappush(self.right_min_heap,num_to_move)
        
        if not self.right_min_heap:
            return
        
        if self.right_min_heap[0]<-self.left_max_heap[0]:
            right_min,left_max= hp.heappop(self.right_min_heap),-hp.heappop(self.left_max_heap)
            hp.heappush(self.left_max_heap,-right_min)
            hp.heappush(self.right_min_heap,left_max)
    
    def findMedian(self) -> float:
        if (len(self.left_max_heap)+len(self.right_min_heap)) %2==0:
            return (-self.left_max_heap[0]+self.right_min_heap[0])/2
        
        return  min(-self.left_max_heap[0],self.right_min_heap[0]) if self.right_min_heap else -self.left_max_heap[0]
        
        
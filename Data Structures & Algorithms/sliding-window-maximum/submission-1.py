import heapq as hp
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res=[]
        counter={}
        heap=[]
        l,r=0,0

        while r-l<k:
            new_num=nums[r]
 
            if new_num not in counter:
                counter[new_num]=0
                hp.heappush(heap,-new_num)
            counter[new_num]+=1
            r+=1
            
        while r<len(nums):
            while counter[-heap[0]]==0:
                del counter[-heap[0]]
                hp.heappop(heap)
            
            max_num=-heap[0]
            res.append(max_num)

            num_to_remove=nums[l]
            counter[num_to_remove]-=1
            
            new_num=nums[r]
            if new_num not in counter:
                counter[new_num]=0
                hp.heappush(heap,-new_num)
            counter[new_num]+=1

            l+=1
            r+=1


        while counter[-heap[0]]==0:
            del counter[-heap[0]]
            hp.heappop(heap)
            
        max_num=-heap[0]
        res.append(max_num)
        return res
        
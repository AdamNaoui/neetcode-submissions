class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        paths=[(0,[])]

        subsets=set()

        while paths:
            index,arr=paths.pop()
            if index>=len(nums):
                subsets.add(tuple(arr))
                continue
            
            paths.append((index+1,arr))
            paths.append((index+1,arr+[nums[index]]))
        
        res=[]

        for subset in subsets:
            res.append(list(subset))
        
        return res
        
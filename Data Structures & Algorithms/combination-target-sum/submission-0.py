class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combi=set()
        paths=[(0,[],0)] # index, array, total

        while paths:
            index,arr,total=paths.pop()
            if total>target:
                continue
            
            if total==target:
                combi.add(tuple(arr))
                continue
            
            if len(nums)<=index:
                continue

            paths.append((index+1,arr,total))
            paths.append((index,arr+[nums[index]],total+nums[index]))
            paths.append((index+1,arr+[nums[index]],total+nums[index]))
        
        res=[]
        for c in combi:
            res.append(list(c))
        return res
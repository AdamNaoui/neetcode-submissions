class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combi=set()
        paths=[(0,[],0)] # index, array, total
        candidates.sort()
        while paths:
            index,arr,total=paths.pop()
            if total>target:
                continue
            
            if total==target:
                combi.add(tuple(arr))
                continue
            
            if len(candidates)<=index:
                continue

            paths.append((index+1,arr,total))
            paths.append((index+1,arr+[candidates[index]],total+candidates[index]))
        
        res=[]
        for c in combi:
            res.append(list(c))
        return res
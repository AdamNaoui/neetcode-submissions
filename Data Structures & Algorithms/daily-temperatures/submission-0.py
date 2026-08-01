class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        best_by_index={}

        stack=[] # store temp,index

        for i,temp in enumerate(temperatures):
            while stack and stack[-1][0]<temp:
                _,prev_index=stack.pop()
                best_by_index[prev_index]=i-prev_index
            
            stack.append((temp,i))
        
        res=[]

        for i in range(len(temperatures)):
            if i not in best_by_index:
                res.append(0)
                continue

            res.append(best_by_index[i])
        return res

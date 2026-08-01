class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]

        remaining_indices=set([i for i in range(len(nums))])

        def dfs(arr):
            if len(arr) ==len(nums):
                res.append(arr)
                return
            
            for nxt_index in list(remaining_indices):
                remaining_indices.remove(nxt_index)
                dfs(arr+[nums[nxt_index]])
                remaining_indices.add(nxt_index)
        
        dfs([])
        return res

        
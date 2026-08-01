class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[[]]
        curr=[]
        def dfs(index):
            if index>=len(nums):
                return
            
            curr.append(nums[index])
            copy=[num for num in curr]
            res.append(copy)
            dfs(index+1)
            
            curr.pop()
            dfs(index+1)
        
        dfs(0)

        return res

        
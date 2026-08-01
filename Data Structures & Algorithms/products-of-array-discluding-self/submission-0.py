class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_to_right=[1]
        right_to_left=[1]
        for num in nums:
            left_to_right.append(left_to_right[-1]*num)

        for i in range(len(nums)-1,-1,-1):
            right_to_left.append(right_to_left[-1]*nums[i])
        right_to_left=list(reversed(right_to_left))
    
        res=[]
        for i in range(len(nums)):
            res.append(left_to_right[i]*right_to_left[i+1])
        return res

        


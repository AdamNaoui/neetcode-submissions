class Solution:
    def trap(self, height: List[int]) -> int:
        max_left=[0]
        for i in range(1,len(height)):
            max_left.append(max(max_left[-1],height[i-1]))
        
        max_right=[0]
        for i in range(len(height)-2,-1,-1):
            max_right.append(max(max_right[-1],height[i+1]))
        
        max_right.reverse()
        
        res=0

        for i in range(len(height)):
            curr_height=height[i]
            min_bound=min(max_left[i],max_right[i])
            res+=max(0,min_bound-curr_height)
        return res
        
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res=0
        stack=[(-1,0,-1)] # store index, last max height, total prev area
        seen=set()
        while stack:
            curr_index,last_max_height,area_start_index=stack.pop()
            if(curr_index,last_max_height,area_start_index) in seen:
                continue
            seen.add((curr_index,last_max_height,area_start_index))
            curr_area=(curr_index-area_start_index+1)*last_max_height
            res=max(res,curr_area)
            if curr_index+1>=len(heights):
                continue
            
            next_height=heights[curr_index+1]
            if next_height<=last_max_height:
                stack.append((curr_index+1,next_height,area_start_index))
                continue
            
            stack.append((curr_index+1,last_max_height,area_start_index))
            stack.append((curr_index+1,next_height,curr_index+1))
        
        return res


        
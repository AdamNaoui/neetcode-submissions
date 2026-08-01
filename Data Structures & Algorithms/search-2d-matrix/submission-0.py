class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS,COLS=len(matrix),len(matrix[0])
        top,bottom=0,ROWS-1

        # find target row
        target_row=-1
        while top<=bottom:
            mid_row=top +(bottom-top)//2

            if matrix[mid_row][0] <=target<=matrix[mid_row][COLS-1]:
                target_row=mid_row
                break
            
            if matrix[mid_row][0] > target:
                bottom=mid_row-1
                continue
            top=mid_row+1
        
        if target_row==-1:
            return False
        

        left,right=0,COLS-1
        while left<=right:
            mid_col=left+(right-left)//2
            mid_num=matrix[target_row][mid_col]

            if mid_num==target:
                return True
            
            if mid_num < target:
                left=mid_col+1
                continue
            
            right=mid_col-1
        
        return False


        
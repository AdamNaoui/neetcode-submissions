class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS,COLS=len(grid),len(grid[0])

        max_area=0
        seen=set()

        deltas=[(-1,0),(1,0),(0,-1),(0,1)]
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col]==0:
                    continue
                
                if (row,col) in seen:
                    continue

                count=0
                pos=[(row,col)]

                while pos:
                    row,col=pos.pop()

                    if (row,col) in seen:
                        continue

                    count+=1
                    max_area=max(max_area,count)
                    seen.add((row,col))

                    for dx,dy in deltas:
                        new_row,new_col=row+dx,col+dy
                        if 0<=new_row<ROWS and 0<=new_col<COLS and grid[new_row][new_col]==1:
                            pos.append((new_row,new_col))
        return max_area


                    

                
        
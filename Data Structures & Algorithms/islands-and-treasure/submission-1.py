class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS,COLS = len(grid), len(grid[0])
        INF=2147483647
        deltas=[(-1,0),(1,0),(0,1),(0,-1)]

        for row in range(ROWS):
            for col in range(COLS):
                #find chest

                if grid[row][col]!=0:
                    continue
                
                seen=set()

                pos=[(row,col,0)]
                while pos:
                    row,col,dist = pos.pop(0)
                    if (row,col) in seen:
                        continue

                    seen.add((row,col))

                    if grid[row][col]<0:
                        continue
                    
                    
                    if dist>grid[row][col] and dist>0:
                        continue

                    grid[row][col]=dist
        
                    for dx,dy in deltas:
                        if 0<=row+dx<ROWS and 0<=col+dy<COLS:
                            pos.append((row+dx,col+dy,dist+1))

                    




        
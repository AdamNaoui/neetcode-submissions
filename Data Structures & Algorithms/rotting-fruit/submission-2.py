class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten=[]
        fresh_count=0
        fresh={}

        ROWS,COLS= len(grid),len(grid[0])
        deltas=[(-1,0),(1,0),(0,-1),(0,1)]

        for row in range(ROWS):
            for col in range(COLS):
                cell=grid[row][col]
                
                if cell==0:
                    continue
                
                if cell==1:
                    fresh_count+=1
                    continue
                
                rotten.append((row,col))

        if fresh_count==0:
            return 0

        for row,col in rotten:
            pos=[(row,col,0)]
            seen=set()
            while pos:
                r,c,time=pos.pop(0)
                if (r,c) in seen:
                    continue
                
                seen.add((r,c))

                if grid[r][c]==0:
                    continue
                
                if grid[r][c] ==1:
                    if (r,c) not in fresh:
                        fresh[(r,c)]=time
                    
                    elif fresh[(r,c)]<=time:
                        continue
                    
                    fresh[(r,c)]=min(fresh[(r,c)],time)

                for dx,dy in deltas:
                    if 0<=r+dx<ROWS and 0<=c+dy<COLS:
                        pos.append((r+dx,c+dy,time+1))
        
        if len(fresh)<fresh_count:
            return -1
        
        return max(fresh.values())
        

        
        





                

        
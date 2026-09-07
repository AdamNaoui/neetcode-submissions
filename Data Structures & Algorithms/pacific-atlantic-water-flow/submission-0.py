class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        # check pacific
        p_seen=set()

        ROWS,COLS=len(heights),len(heights[0])

        pacific=[(row,0) for row in range(ROWS)] + [(0,col) for col in range(COLS)]

        for row,col in pacific:
            p_seen.add((row,col))

        while pacific:
            row,col=pacific.pop()

            for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                if not (0<=row+dx<ROWS) or not (0<=col+dy<COLS):
                    continue
                
                if heights[row+dx][col+dy]<heights[row][col]:
                    continue
                
                if (row+dx,col+dy) in p_seen:
                    continue
                
                pacific.append((row+dx,col+dy))

                p_seen.add((row+dx,col+dy))
        
        # check atlantic
        a_seen=set()
        atlantic=[(row,COLS-1) for row in range(ROWS)] + [(ROWS-1,col) for col in range(COLS)]

        for row,col in atlantic:
            a_seen.add((row,col))

        while atlantic:
            row,col=atlantic.pop()

            for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                if not (0<=row+dx<ROWS) or not (0<=col+dy<COLS):
                    continue
                
                if heights[row+dx][col+dy]<heights[row][col]:
                    continue
                
                if (row+dx,col+dy) in a_seen:
                    continue
                
                atlantic.append((row+dx,col+dy))

                a_seen.add((row+dx,col+dy))
    
        union=a_seen.intersection(p_seen)
        print(union)
        return [[row,col] for row,col in union]
        
            
            


        
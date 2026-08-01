class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen=set()
        count=0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row,col) in seen:
                    continue
                if grid[row][col]=="0":
                    continue
                
                bfs=[(row,col)]
                count+=1
                while bfs:
                    curr_row,curr_col=bfs.pop()
                    if (curr_row,curr_col) in seen:
                        continue

                    seen.add((curr_row,curr_col))

                    for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                        if not (0<=(curr_row + dx)<len(grid)) or not (0<=(curr_col + dy)<len(grid[0])):
                            continue
                        if grid[curr_row + dx][curr_col + dy] == "1":

                            bfs.append((curr_row + dx, curr_col + dy))
        return count
                    
                        



        
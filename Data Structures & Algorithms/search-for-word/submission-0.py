class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited_cells=set()
        ROWS,COLS =len(board),len(board[0])
        deltas=[(1,0),(-1,0),(0,1),(0,-1)]

        def dfs(w_index,cell):
            if w_index==len(word):
                return True

            if cell in visited_cells:
                return False
            
            row,col=cell
            if not (0<=row<ROWS) or not (0<=col<COLS):
                return False
            
            if board[row][col]!=word[w_index]:
                return False
            
            visited_cells.add(cell)
            
            for dr,dc in deltas:
                if dfs(w_index+1,(row+dr,col+dc)):
                    return True
            
            visited_cells.remove(cell)
            return False
        
        for row in range(ROWS):
            for col in range(COLS):
                if dfs(0,(row,col)):
                    return True
        
        return False
        
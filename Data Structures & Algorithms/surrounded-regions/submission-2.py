class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS,COLS=len(board),len(board[0])

        seen=set()

        to_check=[]

        for row in range(ROWS):
            if board[row][0] == 'X':
                    continue
            to_check.append((row,0))     
        for row in range(ROWS):
            if board[row][COLS-1] == 'X':
                    continue
            to_check.append((row,COLS-1))

        for col in range(COLS):
            if board[0][col] == 'X':
                    continue
            to_check.append((0,col))   

        for col in range(COLS):
            if board[ROWS-1][col] == 'X':
                    continue
            to_check.append((ROWS-1,col))   


        while to_check:
            row,col = to_check.pop()

            if (row,col) in seen:
                continue

            seen.add((row,col))

            for (dx,dy) in [(-1,0),(0,-1),(1,0),(0,1)]:
                new_x,new_y=row+dx,col+dy
                if not 0<=new_x<ROWS or not 0<=new_y<COLS or board[new_x][new_y]!="O":
                    continue
                   
                to_check.append((new_x,new_y))

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col]!="O":
                    continue
                
                if (row,col) in seen:
                    continue
                
                board[row][col]="X"

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res=[]
        queue=[[]]
        while queue:
            curr_state=queue.pop()
            #print(curr_state)
            next_row=len(curr_state)
            if len(curr_state) == n:
                res.append(curr_state)
                continue
            
            queens_pos=[]
            for i,row_state in enumerate(curr_state):
                queens_pos.append((i,row_state.index('Q')))
        
            for next_col in range(n):
                valid=True
                for queen_row,queen_col in queens_pos:
                    #print(queen_row,queen_col)
                    #print(next_row)
                    if queen_row ==next_row or queen_col ==next_col or abs(queen_row-next_row)==abs(queen_col-next_col):
                        valid=False
                        break
                    
                if valid:
                    next_row_state=next_col*"."+"Q"+(n-next_col-1)*"."
                    queue.append(curr_state+[next_row_state])





        return res
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows
        for row in range(9):
            seen=set()
            for col in range(9):
                num=board[row][col]
                if num ==".":continue
                if num in seen:
                    return False
                seen.add(num)
        
        # check cols
        for col in range(9):
            seen=set()
            for row in range(9):
                num=board[row][col]
                if num ==".":continue
                if num in seen:
                    return False
                seen.add(num)
        
        #check squares
        for i in range(0,9,3):
            for j in range(0,9,3):
                seen=set()
                for new_r in range(i,i+3,1):
                    for new_c in range(j,j+3,1):
                        num=board[new_r][new_c]
                        if num ==".":continue
                        if num in seen:
                            return False
                        seen.add(num)
        return True
        
        
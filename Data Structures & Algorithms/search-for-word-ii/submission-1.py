class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Step 1 do a prefix trie for words put special key  ie ("":word) when we reach end of a word
        trie={}
        
        for word in words:
            curr_node=trie
            for i,char in enumerate(word):
                if char not in curr_node:
                    curr_node[char]={}
                
                curr_node=curr_node[char]

                if i==len(word)-1:
                    curr_node[""]=word

        res=set()

        # Step 2 do dfs while prefix trie can handle path (keep a visited cells set to not go backward)
        ROWS,COLS=len(board),len(board[0])
        deltas=[(0,1),(1,0),(0,-1),(-1,0)]
        visited_cells=set()

        def dfs(curr_cell,curr_trie_node):
            row,col=curr_cell
            
            if not (0<=row<ROWS) or not (0<=col<COLS) or (row,col) in visited_cells:
                return
            
            char=board[row][col]

            if char not in curr_trie_node:
                return
            
            new_trie_node=curr_trie_node[char]

            if "" in new_trie_node:
                # Step 3 add to answer set the word when reaching a word and continue
                res.add(new_trie_node[""])
            
            visited_cells.add(curr_cell)
 
            for dx,dy in deltas:
                dfs((row+dx,col+dy),new_trie_node)
            
            visited_cells.remove(curr_cell)
        
        for row in range(ROWS):
            for col in range(COLS):
                dfs((row,col),trie)
        
        # Step 4 return the list of the set

        return list(res)

class WordDictionary:

    def __init__(self):
        self.trie={}
        

    def addWord(self, word: str) -> None:
        curr_node=self.trie

        for char in word:
            if char not in curr_node:
                curr_node[char]={}
            
            curr_node=curr_node[char]
        
        curr_node[""]=True

    def search(self, word: str) -> bool:
        curr_node=self.trie
        candidates=[(0,curr_node)] # index of word and curr_node

        while candidates:
            i,node=candidates.pop()
            print(i,node)
            if i==len(word):
                if "" in node:
                    return True
                continue

            # i < len(word)
            char=word[i]

            if char not in node and char != '.':
                continue
            
            if char in node:
                candidates.append((i+1,node[char]))
                continue
            
            for next_node in node.values():
                if next_node is True:
                    continue
                candidates.append((i+1,next_node))

        return False
                

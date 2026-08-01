class PrefixTree:

    def __init__(self):
        self.trie={}
        self.words=set()
        

    def insert(self, word: str) -> None:
        self.words.add(word)
        curr_node=self.trie
        for char in word:
            if char not in curr_node:
                curr_node[char]={}
            curr_node=curr_node[char]


    def search(self, word: str) -> bool:
        return word in self.words

        

    def startsWith(self, prefix: str) -> bool:
        curr_node=self.trie
        for char in prefix:
            if char not in curr_node:
                return False
            
            curr_node=curr_node[char]
        return True
        
        
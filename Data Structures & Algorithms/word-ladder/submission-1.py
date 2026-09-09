class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList.append(beginWord)
        graph={word:[] for word in wordList}
        
        for i,word in enumerate(wordList):
            for j in range(i+1,len(wordList)):
        
                next_word=wordList[j]
                joker=0
                
                for k in range(len(word)):
                    if word[k] == next_word[k]:
                        continue

                    joker+=1

                    if joker == 2:
                        break
                    
                if joker<2:
                    graph[word].append(next_word)
                    graph[next_word].append(word)
        

        seen=set()
        paths=[(beginWord,1)]
        while paths:
            word,dist=paths.pop(0)
            if word == endWord:
                return dist
            
            if word in seen or word not in graph:
                continue
            
            seen.add(word)

            for next_word in graph[word]:
                if next_word in seen:
                    continue
                
                paths.append((next_word,dist+1))
            
        return 0



        
        
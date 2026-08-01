class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        #are they all connected?
        graph={i:set() for i in range(n)}

        for [a,b] in edges:
            graph[a].add(b)
            graph[b].add(a)
        
        seen=set()
        nodes=[0]

        while nodes:
            node = nodes.pop(0)
            seen.add(node)
            for nxt in graph[node]:
                graph[nxt].remove(node)
                if nxt in seen or nxt in nodes:
                    return False
                
                nodes.append(nxt)
        
        return len(seen)==n
                

                

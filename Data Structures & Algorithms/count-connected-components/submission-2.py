class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        left= set()
        for i in range(n):
            left.add(i)
        
        graph={i:[] for i in range(n)}
        for [a,b] in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        res=0
        while left:
            node=next(iter(left))
            nodes=[node]
            res+=1
            while nodes:
                curr=nodes.pop()
                left.remove(curr)
                for nxt in graph[curr]:
                    if nxt not in left or nxt in nodes:
                        continue
                    
                    nodes.append(nxt)
        return res
        
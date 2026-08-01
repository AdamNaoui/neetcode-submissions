class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        deps={c: set() for c in range(numCourses)}
        allow={c: set() for c in range(numCourses)}

        for [nxt,prv] in prerequisites:
            deps[nxt].add(prv)
            allow[prv].add(nxt)
        

        available=[]
        for c in range(numCourses):
            if not deps[c]:
                available.append(c)
        
        print(available)
        res=[]

        while available:
            c=available.pop()
            res.append(c)

            for nxt in allow[c]:
                deps[nxt].remove(c)
                
                if not deps[nxt]:
                    available.append(nxt)
        
                
        return res if len(res) == numCourses else []
        
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        possibilities=[([],"")] # store stack, and string
        res=[]

        while possibilities:
            stack,string=possibilities.pop()
            if len(string)==n*2:
                if len(stack)==0:
                    res.append(string)
                continue
            
            possibilities.append((stack+["("],string+"("))

            if stack and stack[-1]=="(":
                stack.pop()
                possibilities.append((stack,string+")"))
        
        return res


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]

        operators={"*","+","-","/"}
        for token in tokens:
            print(stack)
            if token not in operators:
                stack.append(int(token))
                continue
            
            a,b=stack.pop(),stack.pop()

            if token=="+":
                stack.append(a+b)
                continue
            if token=="*":
                stack.append(a*b)
                continue
            
            if token=="-":
                stack.append(b-a)
                continue
            
            if token=="/":
                
                if b/a <0:
                    stack.append(math.ceil(b/a))
                else:
                    stack.append(math.floor(b/a))
        
        return stack[-1]
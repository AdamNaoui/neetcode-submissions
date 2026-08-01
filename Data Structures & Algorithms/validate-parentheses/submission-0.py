class Solution:
    def isValid(self, s: str) -> bool:
        openings_and_closing={"(":")","[":"]","{":"}"}
        stack=[]
        for char in s:
            if char in openings_and_closing:
                stack.append(char)
                continue

            if not stack or char != openings_and_closing[stack[-1]]:
                return False
            
            stack.pop()

        return len(stack)==0
        
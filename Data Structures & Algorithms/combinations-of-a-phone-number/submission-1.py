class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        corrs={
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }

        res=[]

        paths=[("",0)]

        while paths:
            rep,index=paths.pop()
            if index>=len(digits):
                res.append(rep)
                continue
        
            digit=digits[index]
     
            corr=corrs[digit]
            for char in corr:         
                paths.append((rep+char,index+1))
        
        return res

        
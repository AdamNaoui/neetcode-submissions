class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for string in strs:
            length=len(string)
            res+=str(length)+":"+string
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        i=0
        res=[]
        while i <len(s):
            length=""
            while s[i]!=":":
                length+=s[i]
                i+=1
    
            num_length=int(length)
            sub_string=s[i+1:i+num_length+1]
            res.append(sub_string)
            i+=num_length+1

        return res


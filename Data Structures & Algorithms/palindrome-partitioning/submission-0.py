class Solution:
    def isPalindrome(self,s,l,r):
        left,right=l,r

        while left<right:
            if s[left]!=s[right]:
                return False
            left+=1
            right-=1
        return True
    
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        paths=[([],0,0)] # store curr_partioning , left index and curr_index

        while paths:
            curr_part,left,curr=paths.pop()
            if curr>=len(s) and left>=len(s):
                res.append(curr_part)
                continue
            
            if curr>=len(s):
                continue
            
            paths.append((curr_part,left,curr+1))
            # check if left to curr is palindrome
            if self.isPalindrome(s,left,curr):
                paths.append((curr_part+[s[left:curr+1]],curr+1,curr+1))
            
        return res
        
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):return False

        s_chars_count={}

        for char in s:
            if char not in s_chars_count:
                s_chars_count[char]=0
            s_chars_count[char]+=1
        

        # check t

        for char in t:
            if char not in s_chars_count:
                return False
            s_chars_count[char]-=1
            if s_chars_count[char] ==0:
                del s_chars_count[char]
        return True


        
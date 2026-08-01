class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen={} # char -> last index
        res,l,r=0,0,0
        while r<len(s):
            new_char=s[r]
            if new_char not in seen or seen[new_char]<l:
                seen[new_char]=r
                res=max(res,r-l+1)
                r+=1
                continue
            
            last_index_of_char=seen[new_char]
            l=last_index_of_char+1
            seen[new_char]=r
            r+=1
        return res

            


        
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_chars_counter={}
        for char in t:
            if char not in t_chars_counter:
                t_chars_counter[char]=0
            t_chars_counter[char]+=1
        
        res_indices=(-1,-1)


        l,r=0,0
        t_chars_covered=set()

        while l<=r and r<len(s):
            char_to_add=s[r]
            if char_to_add in t_chars_counter:
                t_chars_counter[char_to_add]-=1

                if t_chars_counter[char_to_add]<=0:
                    t_chars_covered.add(char_to_add)
            
            contains_sub_string=len(t_chars_covered)==len(t_chars_counter)
            res_already_exist= res_indices!=(-1,-1)

            # minimse substring from the left
            while contains_sub_string and l<=r:
                print(l,r)
                if not res_already_exist or r-l < res_indices[1]-res_indices[0]:
                    res_indices=(l,r)
                
                char_to_remove=s[l]
                if char_to_remove in t_chars_counter:
                    t_chars_counter[char_to_remove]+=1
                    if t_chars_counter[char_to_remove] >0 and char_to_remove in t_chars_covered:
                        t_chars_covered.remove(char_to_remove)
                
                contains_sub_string=len(t_chars_covered)==len(t_chars_counter)
                res_already_exist= res_indices!=(-1,-1)
                l+=1
            
            #expand from the right
            r+=1


        if res_indices == (-1,-1):
            return ""
        
        l,r=res_indices
        return s[l:r+1]

        
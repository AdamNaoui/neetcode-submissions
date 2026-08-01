class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False

        s1_counter={}

        for char in s1:
            if char not in s1_counter:
                s1_counter[char]=0
            s1_counter[char]+=1
        
        chars_covered_by_sw=set()
  
        l,r=0,0
        while r-l+1 <=len(s1):
            char=s2[r]
            if char in s1_counter:
                s1_counter[char]-=1
                if s1_counter[char]<=0:
                    chars_covered_by_sw.add(char)
            r+=1
        
        if len(chars_covered_by_sw)==len(s1_counter):
                return True

        while r<len(s2):
            char_to_remove=s2[l]
            char_to_add=s2[r]

            if char_to_remove in s1_counter:
                s1_counter[char_to_remove]+=1
                if s1_counter[char_to_remove]>0 and char_to_remove in chars_covered_by_sw :
                    chars_covered_by_sw.remove(char_to_remove)

            if char_to_add in s1_counter:
                s1_counter[char_to_add]-=1
                if s1_counter[char_to_add]<=0:
                    chars_covered_by_sw.add(char_to_add)
            
            if len(chars_covered_by_sw)==len(s1_counter):
                return True

            r+=1
            l+=1
        return len(chars_covered_by_sw)==len(s1_counter)




        
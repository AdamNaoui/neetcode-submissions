class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_by_char={}
        chars_by_freq={}
        max_freq=1
        max_freq_counts=0
        l,r=0,0
        res=1
        while r<len(s):
            new_char=s[r]
            if ((new_char in freq_by_char and freq_by_char[new_char]==max_freq)  or max_freq+k>=r-l+1) and r<len(s):
               # print(l,r,max_freq)
                
                if new_char not in freq_by_char:
                    freq_by_char[new_char]=0

                freq_by_char[new_char]+=1

                if freq_by_char[new_char] > max_freq:
                    max_freq=freq_by_char[new_char]
                    max_freq_counts=1

                elif freq_by_char[new_char]==max_freq:
                    max_freq_counts+=1

                res=max(res,r-l+1) 
                if res==r-l+1:
                    print(s[l:r+1])
                r+=1
                continue
        
            
            old_char=s[l]
            #print("old",l,r,old_char)
            if freq_by_char[old_char]== max_freq:
                max_freq_counts-=1
            
            if max_freq_counts==0:
                max_freq=max(max_freq-1,1)
                max_freq_counts=1

            freq_by_char[old_char]-=1
            l+=1

        return res



        
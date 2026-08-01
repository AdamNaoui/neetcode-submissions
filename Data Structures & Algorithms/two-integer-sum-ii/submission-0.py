class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r=0,len(numbers)-1

        while l<r:
            l_num= numbers[l]
            r_num= numbers[r]

            if l_num+r_num ==target:
                return [l+1,r+1]
            
            if l_num+r_num>target:
                r-=1
                continue
            
            l+=1
        return False
        
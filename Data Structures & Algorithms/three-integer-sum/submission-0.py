class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        res=[]
        seen=set()
        print(nums)
        for pivot in range(len(nums)):
            pivot_num=nums[pivot]
            l,r=pivot+1,len(nums)-1
            while l<r:
                l_num,r_num=nums[l],nums[r]
                if pivot_num+l_num+r_num==0:
                    if (pivot_num,l_num,r_num) not in seen:
                        res.append([pivot_num,l_num,r_num])
                        seen.add((pivot_num,l_num,r_num))
                    l+=1
                    continue
                
                if pivot_num+l_num+r_num>0:
                    r-=1
                    continue

                l+=1
        return res

        
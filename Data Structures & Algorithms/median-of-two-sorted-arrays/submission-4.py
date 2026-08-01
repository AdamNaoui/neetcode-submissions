class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if not nums1 and not nums2:
            return float("nan")
        if not nums1:
            return nums2[len(nums2)//2] if len(nums2)%2==1 else (nums2[len(nums2)//2]+nums2[-1+len(nums2)//2])/2
        if not nums2:
            return nums1[len(nums1)//2] if len(nums1)%2==1 else (nums1[len(nums1)//2]+nums1[-1+len(nums1)//2])/2

        total_len=len(nums1)+len(nums2)
        target_offset= -1+ total_len//2 if total_len %2==0 else total_len//2
        
        l1,r1=0,len(nums1)-1
        l2,r2=0,len(nums2)-1

        print(target_offset)
        while l1+l2<target_offset and l1<=r1 and l2<=r2:
            mid1=l1+(r1-l1)//2
            mid2=l2+(r2-l2)//2
            #print(l1,r1)
            #print(l2,r2)
            if mid1+mid2<target_offset:
                if nums1[mid1]>=nums2[mid2]:
                    l2=mid2+1
                    continue
                l1=mid1+1
                continue
            
            if mid1+mid2==target_offset:
                if nums1[mid1]>=nums2[mid2]:
                    if l2!=mid2:
                        l2=mid2
                    else:
                        l2=mid2+1
                    continue
                if l1!=mid1:
                    l1=mid1
                else:
                    l1=mid1+1
                    
                
                continue

         
            if nums1[mid1]>=nums2[mid2]:
                r1=mid1-1
                continue

            r2=mid2-1
            
        
        print(l1,r1)
        print(l2,r2)
        if l1>r1:
            target_offset-=l1
            target_offset-=l2
            return nums2[l2+target_offset] if (len(nums2)+len(nums1))%2==1 else  (nums2[l2+target_offset+1]+nums2[l2+target_offset])/2
        
        if l2>r2:
            target_offset-=l1
            target_offset-=l2
            return nums1[l1+target_offset] if (len(nums2)+len(nums1))%2==1 else  (nums1[l1+target_offset+1]+nums1[l1+target_offset])/2
        
        vals=[]
        if l1<len(nums1):
            vals.append(nums1[l1])
            if l1+1<len(nums1):
                vals.append(nums1[l1+1])

        if l2<len(nums2):
            vals.append(nums2[l2])
            if l2+1<len(nums2):
                vals.append(nums2[l2+1])
        vals.sort()

        if (len(nums2)+len(nums1))%2==1:
            return vals[0]
        else:
            return (vals[0]+vals[1])/2
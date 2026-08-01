class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen=set()
        
        for num in nums:
            if num not in seen:
                seen.add(num)
        
        buckets={} # bucket by num it should share same bucket, a set
        res=0
        for num in nums:
            left_bucket=None if num -1 not in buckets else buckets[num-1]
            right_bucket=None if num +1 not in buckets else buckets[num+1]

            if not left_bucket and not right_bucket:
                new_bucket=set()
                new_bucket.add(num)
                buckets[num]=new_bucket
                continue
            
            if not right_bucket:
                left_bucket.add(num)
                buckets[num]=left_bucket
                continue
            if not left_bucket:
                right_bucket.add(num)
                buckets[num]=right_bucket
                continue
            
            new_bucket=left_bucket.union(right_bucket)
            new_bucket.add(num)

            for l_num in left_bucket:
                buckets[l_num]=new_bucket
            buckets[num]=new_bucket
            for r_num in right_bucket:
                buckets[r_num]=new_bucket
        
        for bucket in buckets.values():
            res=max(res,len(bucket))
        return res

                


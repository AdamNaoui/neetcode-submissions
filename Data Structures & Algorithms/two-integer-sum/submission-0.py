class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={} # store num as key and index as val

        for i,num in enumerate(nums):
            if target-num in seen:
                return [seen[target-num],i]
            
            seen[num]=i
            
        
import heapq as hp
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        # Sort intervals by end time to use a greedy approach
        intervals.sort(key=lambda x: x[1])
        
        res = 0
        # Track the end time of the last added non-overlapping interval
        prev_end = float('-inf')
        
        for start, end in intervals:
            if start >= prev_end:
                # No overlap, update the last end time
                prev_end = end
            else:
                # Overlap detected, increment removal count
                res += 1

        return res
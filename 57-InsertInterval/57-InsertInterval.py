# Last updated: 6/4/2025, 2:23:11 PM
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]       

        intervals.append(newInterval)
        intervals.sort()
        
        result = [intervals[0]]
        i = 0
        valid = True

        while i < len(intervals):
            last = result[-1]
            curr = intervals[i]
            
            if curr[0] <= last[1]:
                result[-1][1] = max(last[1], curr[1])
                i += 1
            else:
                result.append(curr)
                i += 1

        return result  
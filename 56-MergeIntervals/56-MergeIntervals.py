# Last updated: 6/4/2025, 1:51:57 PM
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()

        result = [intervals[0]]

        for i in range(1, len(intervals)):
            last = result[-1]
            curr = intervals[i]

            if curr[0] <= last[1]:
                result[-1][1] = max(last[1], curr[1])
            else:
                result.append(curr)

        return result

            

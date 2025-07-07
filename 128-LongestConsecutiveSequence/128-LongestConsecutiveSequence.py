# Last updated: 7/7/2025, 6:20:04 PM
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numbers = set(nums)
        totalLength = 0
        for num in numbers:
            currLength = 0
            if num - 1 not in numbers:
                temp = num
                while temp in numbers:
                    currLength += 1
                    temp += 1

            totalLength = max(totalLength, currLength)

        return totalLength



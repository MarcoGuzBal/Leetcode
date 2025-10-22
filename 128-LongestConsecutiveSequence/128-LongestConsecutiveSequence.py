# Last updated: 10/22/2025, 12:20:37 PM
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        setNums = set(nums)
        longestConsecutive = 0

        for num in setNums:
            if (num - 1) in setNums:
                longestConsecutive = max(1, longestConsecutive)
            else:
                currNum = num + 1
                len = 1
                while currNum in setNums:
                    currNum += 1
                    len += 1
                longestConsecutive = max(len, longestConsecutive)

        return longestConsecutive




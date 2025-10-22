# Last updated: 10/22/2025, 12:21:33 PM
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        setNums = set(nums)
        longestConsecutive = 1

        for num in setNums:
            if (num - 1) not in setNums:
                currNum = num + 1
                len = 1
                while currNum in setNums:
                    currNum += 1
                    len += 1
                longestConsecutive = max(len, longestConsecutive)

        return longestConsecutive




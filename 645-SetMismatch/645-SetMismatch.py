# Last updated: 6/4/2025, 11:40:25 AM
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        l = len(nums)
        i = 0

        while i < l:
            corrIndex = nums[i] - 1
            if nums[i] != nums[corrIndex]:
                nums[i], nums[corrIndex] = nums[corrIndex], nums[i]
            else:
                i += 1

        for i in range(l):
            if i + 1 != nums[i]:
                return [nums[i], i + 1]
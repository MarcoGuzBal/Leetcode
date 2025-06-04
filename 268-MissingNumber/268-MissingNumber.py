# Last updated: 6/4/2025, 11:20:06 AM
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        length = len(nums)
        i = 0

        while i < length:
            correctIndex = nums[i]
            if nums[i] < length and nums[i] != i:
                nums[i], nums[correctIndex] = nums[correctIndex], nums[i]
            else:
                i += 1

        for i in range(length):
            if nums[i] != i:
                return i

        return len(nums)


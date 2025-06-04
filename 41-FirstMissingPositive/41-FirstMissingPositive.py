# Last updated: 6/4/2025, 12:06:21 PM
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        l = len(nums)
        i = 0

        while i < l:
            corr = nums[i] - 1
            if nums[i] > 0 and nums[i] <= l and nums[i] != nums[corr]:
                nums[i], nums[corr] = nums[corr], nums[i]
            else:
                i += 1

        print(nums)

        for i in range(l):
            if nums[i] != i + 1:
                return i + 1

        return nums[i] + 1
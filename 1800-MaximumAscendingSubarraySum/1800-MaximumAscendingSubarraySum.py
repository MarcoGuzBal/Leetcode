class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        i = 0
        Max = 0
        currMax = 0

        while i < len(nums):
            if i > 0 and nums[i] <= nums[i-1]:
                currMax = nums[i]
            else:
                currMax += nums[i]

            Max = max(Max, currMax)
            i += 1

        return Max
        
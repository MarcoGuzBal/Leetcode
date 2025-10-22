# Last updated: 10/22/2025, 12:42:19 PM
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # Naive Solution: iterating through the array and just ignoring the value you are at

        # Optimal: Prefix and Suffix Products

        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        result = [0] * len(nums)

        for i in range(1, len(nums)):
            prefix[i] = nums[i-1] * prefix[i-1]

        for j in range(len(nums) - 2, -1, -1):
            suffix[j] = nums[j+1] * suffix[j+1]

        for k in range(len(nums)):
            result[k] = prefix[k] * suffix[k]

        return result
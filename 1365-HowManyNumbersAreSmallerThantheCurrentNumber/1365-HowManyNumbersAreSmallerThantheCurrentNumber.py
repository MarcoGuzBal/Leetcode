# Last updated: 4/28/2025, 11:44:05 PM
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        result = [0] * len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    pass
                elif nums[j] < nums[i]:
                    result[i] += 1

        return result


        
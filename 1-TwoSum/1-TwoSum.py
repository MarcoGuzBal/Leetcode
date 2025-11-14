# Last updated: 11/13/2025, 7:21:13 PM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    
                    return [i, j]

        return []
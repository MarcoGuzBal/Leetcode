# Last updated: 10/20/2025, 8:35:07 PM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Time Complexity: O(N)
        # Space Complexity: O(N)

        
        hashmap = {}

        for idx, num in enumerate(nums):
            remainder = target - num

            if remainder in hashmap:
                return [idx, hashmap[remainder]]
            else:
                hashmap[num] = idx
            
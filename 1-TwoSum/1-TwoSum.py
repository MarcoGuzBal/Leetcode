# Last updated: 3/31/2025, 2:45:58 PM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap = {}

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in hashmap:
                return [i, hashmap[diff]]
            else:
                hashmap[nums[i]] = i

                
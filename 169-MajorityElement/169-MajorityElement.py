from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_count = defaultdict(int)
        # more than n/2 times
        count = len(nums) // 2
        for num in nums:
            hash_count[num] += 1
            if hash_count[num] > count:
                return num
            
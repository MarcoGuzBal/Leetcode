# Last updated: 6/27/2025, 2:41:46 PM
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numbers = set(nums) #O(N)
        max_len = 0
        for num in numbers:
            curr = num
            curr_max = 0
            if (curr - 1) not in numbers:
                while curr in numbers:
                    curr += 1
                    curr_max += 1
            max_len= max(max_len, curr_max)

        return max_len


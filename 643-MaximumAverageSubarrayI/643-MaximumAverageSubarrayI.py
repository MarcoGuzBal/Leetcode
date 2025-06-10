# Last updated: 6/10/2025, 12:14:54 PM
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        l = 0
        r = k - 1
        s = sum(nums[l:r + 1])
        res = s / k

        l += 1
        r += 1

        while r < len(nums):
            s -= nums[l - 1]
            s += nums[r]
            res = max(res, s / k)

            l += 1
            r += 1


        return res
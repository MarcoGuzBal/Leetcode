# Last updated: 4/21/2025, 8:57:58 PM
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        result = []

        left = 0
        right = 0

        while right < len(nums):
            
            if right == len(nums) - 1:
                if right - left > 0:
                    result.append(f"{nums[left]}->{nums[right]}")
                else:
                    result.append(f"{nums[left]}")
                break

            elif nums[right + 1] == nums[right] + 1:
                right += 1
            else:
                if right - left > 0:
                    result.append(f"{nums[left]}->{nums[right]}")
                else:
                    result.append(f"{nums[left]}")
                left = right + 1
                right = left

        return result






        
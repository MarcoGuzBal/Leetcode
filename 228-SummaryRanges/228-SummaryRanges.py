# Last updated: 4/21/2025, 8:59:42 PM
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        prev = nums[0]
        rng = [prev]
        ret = []
        for i in range(1, len(nums)):
            if nums[i] - prev > 1:
                st = str(rng[0]) if rng[0] == rng[len(rng) - 1] else str(rng[0]) + '->' + str(rng[len(rng) - 1])
                ret.append(st)
                rng = [nums[i]]
            else:
                rng.append(nums[i])
            prev = nums[i]
        st = str(rng[0]) if rng[0] == rng[len(rng) - 1] else str(rng[0]) + '->' + str(rng[len(rng) - 1])
        ret.append(st)
        return ret

        
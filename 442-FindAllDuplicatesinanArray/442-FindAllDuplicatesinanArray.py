# Last updated: 6/4/2025, 11:50:08 AM
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        l = len(nums)
        i = 0
        result = []

        while i < l:
            corr = nums[i] - 1
            if nums[i] != nums[corr]:
                nums[i], nums[corr] = nums[corr], nums[i]
            else:
                i += 1

        #print(nums)

        for i in range(l):
            if nums[i] != i + 1:
                result.append(nums[i])

        return result

        

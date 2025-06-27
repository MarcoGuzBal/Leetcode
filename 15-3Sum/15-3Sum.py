# Last updated: 6/27/2025, 4:17:12 PM
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # [-4, -1, -1, 0 , 1, 1, 2]
        #  ^                  ^  ^

        nums.sort()
        res = []
        
        for i in range(len(nums)):
            if i >0:
                if nums[i] == nums[i - 1]:
                    continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                sum = nums[i] + nums[l] + nums[r]

                if sum == 0:
                    res.append([nums[i],nums[l],nums[r]])
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif sum < 0:
                    l += 1
                else:
                    r -= 1

        return res

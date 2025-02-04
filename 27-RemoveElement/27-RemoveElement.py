class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        left = 0
        right = len(nums) - 1

        while left <= right:
            while right > 0 and nums[right] == val:
                nums.pop(right)
                right -= 1
            if len(nums) > left and nums[left] == val:
                nums[left], nums[right] = nums[right], nums[left]
                nums.pop(right)
                right -= 1

            left += 1
        
        return len(nums)
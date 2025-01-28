class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            curr = nums[mid]

            if target == curr:
                return mid
            elif (curr > target):
                right = mid - 1
            else:
                left = mid + 1

        if curr < target:
            return mid + 1
        else: 
            return mid



                
        
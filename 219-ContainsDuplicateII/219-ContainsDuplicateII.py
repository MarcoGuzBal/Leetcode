class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        windowSet = set()

        left = 0

        for right in range(len(nums)):
            
            if right - left > k:
                windowSet.remove(nums[left])
                left += 1
            if nums[right] in windowSet:
                return True

            windowSet.add(nums[right])

        return False


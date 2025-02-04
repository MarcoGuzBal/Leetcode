class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        red = 0
        white = 0
        blue = 0

        for i in nums:
            if i == 0:
                red += 1
            elif i == 1:
                white += 1
            else:
                blue += 1

        j = 0   
        while j < red:
            nums[j] = 0
            j += 1
        while j < red + white:
            nums[j] = 1
            j += 1
        while j < red + white + blue:
            nums[j] = 2
            j += 1

        return nums
        

            
        
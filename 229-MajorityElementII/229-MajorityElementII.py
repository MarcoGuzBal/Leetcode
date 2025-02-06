class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        elements = []
        numCounter = Counter(nums)
        
        for num in numCounter:
            if numCounter[num] > len(nums)/3:
                elements.append(num)

        return elements
        
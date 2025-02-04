class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        hashmap = defaultdict(int)
        count = len(nums) // 2

        for i in nums:
            hashmap[i] += 1
            if hashmap[i] > (count):
                return i
                

        
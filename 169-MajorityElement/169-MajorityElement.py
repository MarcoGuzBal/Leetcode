class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        hashmap = defaultdict(int)

        for i in range(len(nums)):
            hashmap[nums[i]] += 1
            if hashmap[nums[i]] > (len(nums) // 2):
                return nums[i]
                

        
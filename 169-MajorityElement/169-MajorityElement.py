class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # hashmap = defaultdict(int)
        # count = len(nums) // 2

        # for i in nums:
        #     hashmap[i] += 1
        #     if hashmap[i] > (count):
        #         return i

        count = 0
        candidate = 0

        for i in nums:
            if count == 0:
                candidate = i
                count += 1
            elif i != candidate:
                count -= 1
            else:
                count += 1

        return candidate

                

        
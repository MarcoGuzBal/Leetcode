class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        goodPair = 0
        dictionary = defaultdict(list)

        for i in range(len(nums)):
            dictionary[nums[i]].append(i)

        for i in range(len(nums)):
            currNum = nums[i]
            for j in (dictionary[currNum]):
                if i == j:
                    continue
                elif i < j:
                    goodPair += 1
        

        return goodPair
        
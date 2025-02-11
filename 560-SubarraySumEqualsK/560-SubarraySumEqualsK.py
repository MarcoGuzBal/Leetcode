class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        res, runSum = 0, 0
        hashmap = {0 : 1}

        for num in nums:
            runSum += num
            rem = runSum - k

            res += hashmap.get(rem, 0)
            hashmap[runSum] = 1 + hashmap.get(runSum, 0)

        return res
                
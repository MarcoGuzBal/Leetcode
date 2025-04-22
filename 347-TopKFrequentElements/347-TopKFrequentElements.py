# Last updated: 4/21/2025, 9:09:05 PM
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter = {}
        result = []

        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1

        print(counter)

        for i in range(k):
            max_val = 0
            curr_max = 0
            for val in counter:
                if counter[val] > max_val:
                    max_val = counter[val]
                    curr_max = val
            result.append(curr_max)
            del counter[curr_max]

        return result
# Last updated: 4/22/2025, 12:22:22 AM
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Brute Force
        # Time Complexity: O(N^2)
        # Space Complexity: O()
        counter = {}
        result = []

        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for key in counter:
            buckets[counter[key]].append(key)


        for i in range(len(buckets)-1, -1, -1):
            for num in buckets[i]:
                result.append(num)
                k -= 1
                if k == 0:
                    return result
            
        return result
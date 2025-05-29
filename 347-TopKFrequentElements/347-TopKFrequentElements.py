# Last updated: 5/28/2025, 9:02:50 PM
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Brute Force
        # Time Complexity: O(N^2)
        # Space Complexity: O()
        # counter = {}
        # result = []

        # for num in nums:
        #     if num in counter:
        #         counter[num] += 1
        #     else:
        #         counter[num] = 1

        # buckets = [[] for _ in range(len(nums) + 1)]

        # for key in counter:
        #     buckets[counter[key]].append(key)


        # for i in range(len(buckets)-1, -1, -1):
        #     for num in buckets[i]:
        #         result.append(num)
        #         k -= 1
        #         if k == 0:
        #             return result
            
        # return result

        hashmap = {}
        result = []

        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for val in hashmap:
            index = hashmap[val]
            buckets[index].append(val)

        print(buckets)

        for i in range(len(buckets) - 1, -1, -1):
            if len(result) == k:
                return result
            while buckets[i]:
                if len(result) == k:
                    return result
                topk = buckets[i].pop()
                result.append(topk)

        




















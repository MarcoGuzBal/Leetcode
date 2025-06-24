# Last updated: 6/24/2025, 5:03:31 PM
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

        hashmap = Counter(nums)
        result = []
        buckets = [[] for _ in range(len(nums) + 1)]
        
        for key in hashmap:
            buckets[hashmap[key]].append(key)

        for i in range(len(buckets)-1, -1, -1):
            bucket = buckets[i]
            print(bucket)
            if k == 0:
                return result
            
            if bucket:
                for num in buckets[i]:
                    if k == 0:
                        return result
                    result.append(num)
                    k -= 1
                    
        
        




















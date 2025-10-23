# Last updated: 10/23/2025, 5:05:35 PM
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts = Counter(nums) # O(n)
        heap = []

        for num in counts:
            heapq.heappush(heap, (counts[num], num)) # (Log n)
            # This is needed because a min heap pops the smallest values and we want top k
            if len(heap) > k:
                heapq.heappop(heap)

        ans = []
        for i in range(k):
            popped = heapq.heappop(heap) #(Logn)
            ans.append(popped[1])

        return ans





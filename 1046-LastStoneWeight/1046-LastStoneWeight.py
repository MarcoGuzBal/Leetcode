# Last updated: 6/23/2025, 5:40:56 PM
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        max_heap = []

        for stone in stones:
            heapq.heappush(max_heap, -stone)

        while len(max_heap) > 1:
            stone1 = -heapq.heappop(max_heap)
            stone2 = -heapq.heappop(max_heap)

            if stone1 != stone2:
                heapq.heappush(max_heap, -(stone1 - stone2))

        if len(max_heap) == 0:
            return 0
        else:
            return -heapq.heappop(max_heap)
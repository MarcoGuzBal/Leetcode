class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        heapStones = [-i for i in stones] # Turns values in array negative

        heapq.heapify(heapStones)

        while len(heapStones) > 1:
            y = -(heapq.heappop(heapStones))
            x = -(heapq.heappop(heapStones))

            print(f"{y} and {x}")
            print(heapStones)

            if x != y:
                heapq.heappush(heapStones, -(y-x))
            
        heapStones.append(0)
        return abs(heapStones[0])
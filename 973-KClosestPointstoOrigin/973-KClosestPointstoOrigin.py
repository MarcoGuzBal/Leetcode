# Last updated: 6/17/2025, 12:46:17 PM
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def distance_to_origin(x,y):
            return math.sqrt( pow(x,2) + pow(y,2) )

        result = []
        min_heap = []
        for point in points:
            x = point[0]
            y = point[1]

            dis = distance_to_origin(x, y)
            heapq.heappush(min_heap, (dis, [x, y]))


        while k != 0:
            result.append(heapq.heappop(min_heap)[1])
            k -= 1
        
        return result
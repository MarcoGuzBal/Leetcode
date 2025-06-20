# Last updated: 6/20/2025, 12:02:35 AM
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        min_heap = []
        merged = []

        if nums1:
            heapq.heappush(min_heap, (nums1.pop(0), 1))
        if nums2:
            heapq.heappush(min_heap, (nums2.pop(0), 2))

        while min_heap:
            val, l = heapq.heappop(min_heap)
            merged.append(val)

            if l == 1:
                if nums1:
                    heapq.heappush(min_heap, (nums1.pop(0), 1))
            else:
                if nums2:
                    heapq.heappush(min_heap, (nums2.pop(0), 2))
        
        print(merged)

        if len(merged) % 2 == 0:
            return ((merged[len(merged) // 2] + merged[(len(merged) // 2) - 1]) / 2.0) 
        else:
            return merged[len(merged) // 2]

# Last updated: 6/6/2025, 1:40:55 PM
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:

        a = 0
        b = 0
        
        result = []

        while a < len(firstList) and b < len(secondList):
            currA = firstList[a]
            currB = secondList[b]

            start = max(currA[0], currB[0])
            end = min(currA[1], currB[1])

            if start <= end:
                result.append([start, end])

            if currA[1] <= currB[1]:
                a += 1
            else:
                b += 1

        return result
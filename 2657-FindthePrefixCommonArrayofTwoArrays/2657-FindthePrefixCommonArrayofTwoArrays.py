# Last updated: 4/29/2025, 12:03:38 AM
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        
        result = [0] * len(A)

        map = {}

        for i, val in enumerate(A):
            map[val] = i

        for j in range(len(B)):
            print(f"J: {j}")
            for k in range(j+1):
                print(f"{map[B[k]]} and {j}")
                if map[B[k]] <= j:
                    result[j] += 1

        return result
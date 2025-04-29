# Last updated: 4/28/2025, 11:33:12 PM
class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        
        sum = 0

        map = {}

        for i, char in enumerate(s):
            map[char] = i

        for j, char in enumerate(t):
            sum += abs(map[char] - j)

        return sum
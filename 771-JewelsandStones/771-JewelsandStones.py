# Last updated: 4/22/2025, 11:17:13 PM
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        Set = set(jewels)
        count = 0

        for stone in stones:
            if stone in Set:
                count += 1

        return count
        
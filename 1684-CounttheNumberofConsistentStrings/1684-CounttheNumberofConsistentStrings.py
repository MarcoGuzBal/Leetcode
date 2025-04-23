# Last updated: 4/22/2025, 11:24:23 PM
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:

        Set = set(allowed)

        count = 0

        for string in words:
            allow = True
            for char in string:
                if char not in Set:
                    allow = False

            if allow:
                count += 1

        return count 
        
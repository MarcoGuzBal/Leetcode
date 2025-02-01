class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        
        map1 = Counter(word1)
        map2 = Counter(word2)
        combined = word1 + word2

        # Instead use Counter

        for letter in combined:
            l1 = map1.get(letter, 0)
            l2 = map2.get(letter, 0)

            if abs(l1 - l2) > 3:
                return False

        return True


        
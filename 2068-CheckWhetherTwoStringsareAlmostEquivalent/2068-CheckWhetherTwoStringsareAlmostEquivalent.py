class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        
        map1 = {}
        map2 = {}
        combined = word1 + word2
        print(combined)

        for char in word1:
            if char in map1:
                map1[char] += 1
            else:
                map1[char] = 1
        
        for char in word2:
            if char in map2:
                map2[char] += 1
            else:
                map2[char] = 1

        print(map1)
        print(map2)
        for letter in combined:
            l1 = map1.get(letter, 0)
            l2 = map2.get(letter, 0)



            if abs(l1 - l2) > 3:
                return False

        return True


        
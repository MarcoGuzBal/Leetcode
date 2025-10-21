# Last updated: 10/20/2025, 8:40:23 PM
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Time Complexity: (K N log N)
        # Space Complexity: (NK) since at most N unique Keys and K unique values

        hashmap = {}
        result = []

        for word in strs:
            sortedWord = "".join(sorted(word))

            if sortedWord in hashmap:
                hashmap[sortedWord].append(word)
            else:
                hashmap[sortedWord] = [word]

        for key in hashmap:
            result.append(hashmap[key])

        return result

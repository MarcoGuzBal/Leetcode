class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        longestPrefix = ""
        index = 0

        while index < len(strs[0]):
            currLetter = strs[0][index]
            print(currLetter)
            for word in strs:
                if (len(word) == index) or (word[index] != currLetter):
                    return longestPrefix
            longestPrefix += currLetter
            index += 1

        return longestPrefix

        
        
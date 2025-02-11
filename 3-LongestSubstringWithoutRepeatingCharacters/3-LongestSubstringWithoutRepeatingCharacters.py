class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        maxLength = 0
        currString = ""
        
        while left < len(s) and right < len(s):
            char = s[right]
            if char in currString:
                maxLength = max(maxLength, len(currString))
                left += 1
                right = left
                currString = "" + s[right-1]
            else:
                currString += char
                right += 1

        maxLength = max(maxLength, len(currString))
        return maxLength
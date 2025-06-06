# Last updated: 6/6/2025, 4:59:27 PM
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0
        r = 0
        seen = set() 
        max_len = 0

        while r < len(s):
            if s[r] in seen:
                max_len = max(len(seen), max_len)
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1
            else:
                seen.add(s[r])
                r += 1

        max_len = max(len(seen), max_len)
        return max_len

        # left = 0
        # right = 0
        # maxLength = 0
        # currString = ""
        
        # while left < len(s) and right < len(s):
        #     char = s[right]
        #     if char in currString:
        #         maxLength = max(maxLength, len(currString))
        #         left += 1
        #         right = left
        #         currString = "" + s[right-1]
        #     else:
        #         currString += char
        #         right += 1

        # maxLength = max(maxLength, len(currString))
        # return maxLength
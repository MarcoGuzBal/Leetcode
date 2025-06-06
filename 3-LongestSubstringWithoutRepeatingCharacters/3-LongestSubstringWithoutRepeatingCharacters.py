# Last updated: 6/6/2025, 4:59:59 PM
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        l, res = 0, 0

        for r in range(len(s)):
            if s[r] in mp:
                l = max(l, mp[s[r]] + 1)
            mp[s[r]] = r
            res = max(res, r - l + 1)
        return res

        
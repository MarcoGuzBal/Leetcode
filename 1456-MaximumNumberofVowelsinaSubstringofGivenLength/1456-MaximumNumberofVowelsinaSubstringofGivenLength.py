# Last updated: 6/10/2025, 12:23:05 PM
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        count = 0
        res = 0
        l = 0
        r = k - 1

        for char in s[l:r + 1]:
            if char in vowels:
                count += 1
        res = count

        l += 1
        r += 1

        while r < len(s):
            if s[l - 1] in vowels:
                count -= 1
            if s[r] in vowels:
                count += 1

            res = max(res, count)

            l += 1
            r += 1

        return res
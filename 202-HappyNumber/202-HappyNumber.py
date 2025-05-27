# Last updated: 5/26/2025, 11:29:03 PM
class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = set()

        while n not in seen:
            seen.add(n)
            num = 0
            
            for digit in str(n):
                num += (int(digit) * int(digit))

            n = num

            if n == 1:
                return True
            if n in seen:
                return False

class Solution:
    def mySqrt(self, x: int) -> int:
        

        left = 0
        right = x
        res = 0

        while left <= right:
            mid = (left + right) // 2
            sq = mid * mid
            
            if sq > x:
                right = mid - 1
            elif sq < x:
                left = mid + 1
                res = mid
            else:
                return mid

        return res


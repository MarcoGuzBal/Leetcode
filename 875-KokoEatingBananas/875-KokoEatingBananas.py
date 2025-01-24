class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        MIN = 1
        MAX = max(piles)

        lowestK = MAX

        while MIN <= MAX:
            print(f"{lowestK}")
            print(f"{MIN} AND {MAX}")
            midK = (MIN + MAX) // 2
            hours = 0
            for num in piles:
                hours += math.ceil(num / midK)
            
            print(f"MidK: {midK}, Hours: {hours}")
            if hours <= h:
                lowestK = min(midK, lowestK)
                MAX = midK - 1
            else:
                MIN = midK + 1

        return lowestK

            



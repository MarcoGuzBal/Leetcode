class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        l = 0
        r = len(people) - 1
        minBoat = 0

        peopleSorted = sorted(people)

        print(people)
        while l <= r:
            if (peopleSorted[r] == limit) or (peopleSorted[r] + peopleSorted[l] > limit):
                minBoat += 1
                r -= 1
            elif (peopleSorted[l] + peopleSorted[r] <= limit):
                l += 1
                r -= 1
                minBoat += 1
            else:
                minBoat += 1
        
        return minBoat



        
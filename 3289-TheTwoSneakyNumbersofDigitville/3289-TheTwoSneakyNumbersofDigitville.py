class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        
        SET = set()
        res = []

        for num in nums:
            if num in SET:
                res.append(num)
            else:
                SET.add(num)

        return res

        
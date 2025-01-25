class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:

        val = 0

        for oper in operations:

            if (oper == "++X") or (oper == "X++"):
                val += 1
            else:
                val = (val) - 1
                

        return val
        
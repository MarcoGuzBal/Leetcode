class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk = []
        for i in operations:
            if i =='C':
                stk.pop()
            elif i =='D':
                d = stk[-1]
                d = 2 * int(d)
                stk.append(d)
            elif i =="+":
                temp1 = stk.pop()
                temp2 = stk.pop()
                temp3 = int(temp1) + int(temp2)
                stk.append(temp2)
                stk.append(temp1)
                stk.append(temp3)
            else:
                stk.append(i)
        score = 0
        while stk:
            score += int(stk.pop())
        return score
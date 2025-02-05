class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for operation in operations:
            print(stack)
            if operation == '+':
                num1 = stack[-1]
                num2 = stack[-2]
                stack.append(num1 + num2)
            elif operation == 'D':
                num1 = stack[-1]
                stack.append(num1*2)
            elif operation == 'C':
                stack.pop()
            else:
                stack.append(int(operation))
        
        if len(stack) == 0:
            return 0
        else:
            return sum(stack)
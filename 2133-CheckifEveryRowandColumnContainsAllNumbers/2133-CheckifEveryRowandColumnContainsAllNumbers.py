class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:

        n = len(matrix)

        for i in range(n):
            rowSet = set()
            for num in matrix[i]:
                rowSet.add(num)
            for j in range(1, n + 1):
                if j not in rowSet:
                    return False

        for i in range(n):
            colSet = set()
            for j in range(n):
                currNum = matrix[j][i]
                colSet.add(currNum)
            for k in range(1, n + 1):
                if k not in colSet:
                    return False

        return True

        
        
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        Set = set()

        

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if (i,j) in Set:
                    continue
                else:
                    currX, currY = i, j
                    currNum = matrix[currX][currY]
                    while (currX >= 0 and currX < len(matrix)) and (currY >= 0 and currY < len(matrix[0])):
                        print(f"{currX}, {currY}")
                        if matrix[currX][currY] == currNum:
                            Set.add((i, j))
                            currX += 1
                            currY += 1
                        else:
                            return False

        return True

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        length = len(mat) * len(mat[0])
        if (r * c) != length: 
            return mat

        flatMatrix = []
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                flatMatrix.append(mat[i][j])

        result = []
        count = 0
        for i in range(r):
            row = []
            for j in range(c):
                row.append(flatMatrix[count])
                count += 1
            result.append(row)

        return result
                

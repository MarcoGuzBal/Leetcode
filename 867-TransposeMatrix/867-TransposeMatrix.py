class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
                    
        result = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                print(f"{i}, {j}")
                if i == j:
                    result[i][j] = matrix[i][j]
                else:
                    result[j][i] = matrix[i][j]
        
        return result
class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        
        n = len(matrix)
        expected_set = set(range(1, n + 1))

        # Check rows
        for row in matrix:
            if set(row) != expected_set:
                return False

        # Check columns
        for col in zip(*matrix):
            if set(col) != expected_set:
                return False

        return True
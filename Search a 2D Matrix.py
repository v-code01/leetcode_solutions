class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == target:
                    return True
        return False
  #Simple search, but the question didn't specify parameters and faster than 94% of solutions

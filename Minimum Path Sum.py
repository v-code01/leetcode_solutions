class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS,COLS = len(grid),len(grid[0])
        res = [[float('inf')] *  (COLS +1) for _ in range(ROWS+1)]
        res[ROWS-1][COLS] = 0
        for i in range(ROWS-1,-1,-1):
            for j in range(COLS-1,-1,-1):
                res[i][j] = min(res[i+1][j], res[i][j+1]) + grid[i][j]
        return res[0][0]

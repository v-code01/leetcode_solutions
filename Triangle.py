class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        prev = triangle[-1]
        for i in range(len(triangle)-2, -1, -1):
            for j in range(i+1):
                prev[j] = triangle[i][j] + min(prev[j], prev[j+1])
        return prev[0]

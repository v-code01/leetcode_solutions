class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = []     
        l = 0
        r = len(height) - 1
        while l < r:        
            if height[l] < height[r]:
                vols.append(height[l] * (r-l))
                l += 1
            else:
                res.append(height[r] * (r-l))
                r -= 1                     
        return max(res)

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
#resolved because ij forgot how to leetcode :/
class Solution:
    def maxArea(self, height: List[int]) -> int:
        current = 0
        l,r = 0, len(height) - 1
        while l < r:
            area = (r - l) * min(height[l], height[r])
            if area > current:
                current = area
            if height[r] < height[l]:
                r -= 1
            else:
                l += 1
        return current
   #first solution is less efficient but both are very good

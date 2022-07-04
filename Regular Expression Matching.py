import re

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return re.fullmatch(p, s)
      
#OK NOW ACTUALLY SOLVING IT INSTEAD OF JUST THAT


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        def dfs(i, j):
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False
            
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")
            
            if j+1 < len(p) and p[j+1] == "*":
                return dfs(i, j+2) or (match and dfs(i+1, j))

            return match and dfs(i+1, j+1)
        
        return dfs(0, 0)
      #35 Minutes Solution :)
